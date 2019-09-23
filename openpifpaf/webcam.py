"""Webcam demo application.

Example commands:
    python3 -m pifpaf.webcam  # usbcam or webcam 0
    python3 -m pifpaf.webcam --source=1  # usbcam or webcam 1

    # streaming source
    python3 -m pifpaf.webcam --source=http://128.179.139.21:8080/video

    # file system source (any valid OpenCV source)
    python3 -m pifpaf.webcam --source=docs/coco/000000081988.jpg

Trouble shooting:
* MacOSX: try to prefix the command with "MPLBACKEND=MACOSX".
"""


import argparse
import time

import PIL
import torch

import cv2  # pylint: disable=import-error
from .network import nets
from . import decoder, show, transforms
import json
import numpy as np
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print('matplotlib is not installed')


class Visualizer(object):
    def __init__(self, processor, args):
        self.processor = processor
        self.args = args

    def __call__(self, first_image, fig_width=8.0, **kwargs):
        if plt is None:
            while True:
                image, all_fields = yield
            return

        if 'figsize' not in kwargs:
            kwargs['figsize'] = (fig_width, fig_width * first_image.shape[0] / first_image.shape[1])

        fig = plt.figure(**kwargs)
        ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
        ax.set_axis_off()
        ax.set_xlim(0, first_image.shape[1])
        ax.set_ylim(first_image.shape[0], 0)
        text = 'OpenPifPaf'
        ax.text(1, 1, text,
                fontsize=10, verticalalignment='top',
                bbox=dict(facecolor='white', alpha=0.5, linewidth=0))
        fig.add_axes(ax)
        mpl_im = ax.imshow(first_image)
        fig.show()

        # visualizer
        if self.args.colored_connections:
            viz = show.KeypointPainter(show_box=False, color_connections=True,
                                       markersize=1, linewidth=6)
        else:
            viz = show.KeypointPainter(show_box=False)
        rk = 0
        json_data = []
        while True:
            image, all_fields = yield
            r = time.time()
            keypoint_sets, _ = self.processor.keypoint_sets(all_fields)
            #print(keypoint_sets,'--------------------------keypoint')
            #print(time.time()-r , 'hcl--------------')
            for i, val in enumerate(keypoint_sets):
                bbox_xcycwh_1 = [0, 0, 0, 0]
                # print(pose[i],'pose')
                p_t = []
                for r in range(len(val)):
                    # if pose[i][r][0] == pose[i][r][1]  == pose[i][r][2] == 0:
                    #if val[r][2] != 0 or val[r][1] != 0 or val[r][0] != 0:
                    p_t.append(val[r])
            #fileObject = open('jsonFile.json', 'a')
            #print(p_t)
            p_t= np.vstack(p_t)
            p_t = p_t.tolist()


            draw_start = time.time()
            while ax.lines:
                del ax.lines[0]
            mpl_im.set_data(image)
            viz.keypoints(ax, keypoint_sets)
            fig.canvas.draw()


            rk = rk+1
            print(rk,'iiiiiiiiiiiiiiiiiiii')
            plt.savefig("./r/%s.jpg"%(str(rk)) )
            print('draw', time.time() - draw_start)
            plt.pause(0.01)
            json_data.append(p_t)
            if len(json_data) ==40:
                with open('jsonFile.json', 'a') as fileObject:
                    jsObj = json.dump(json_data,fileObject)
                    fileObject.close()
        plt.close(fig)


def cli():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    nets.cli(parser)
    decoder.cli(parser, force_complete_pose=False, instance_threshold=0.1, seed_threshold=0.5)
    parser.add_argument('--no-colored-connections',
                        dest='colored_connections', default=True, action='store_false',
                        help='do not use colored connections to draw poses')
    parser.add_argument('--disable-cuda', action='store_true',
                        help='disable CUDA')
    parser.add_argument('--source', default='0',
                        help='OpenCV source url. Integer for webcams. Or ipwebcam streams.')
    parser.add_argument('--scale', default= .4, type=float,#0.1
                        help='input image scale factor')
    args = parser.parse_args()

    # check whether source should be an int
    if len(args.source) == 1:
        args.source = int(args.source)

    # add args.device
    args.device = torch.device('cpu')
    if not args.disable_cuda and torch.cuda.is_available():
        print('cuda?????????????????????????????????????????????????')
        args.device = torch.device('cuda')

    return args


def main():
    args = cli()

    # load model
    model, _ = nets.factory_from_args(args)
    model = model.to(args.device)
    processor = decoder.factory_from_args(args, model)

    last_loop = time.time()
    #capture = cv2.VideoCapture(args.source)
    #capture = cv2.VideoCapture('/home/dabai/project/lighttrack/demo/B29.MP4')
    #capture = cv2.VideoCapture('/home/dabai/project/lighttrack/data/demo/video.mp4')
    #capture = cv2.VideoCapture('/home/dabai/project/lighttrack/data/demo/football2.mp4')
    #capture = cv2.VideoCapture('/home/dabai/project/deep_sort_pytorch/jump2.mp4')
    capture = cv2.VideoCapture('/home/dabai/openpose/1.avi')
    visualizer = None
    while True:
        _, image_original = capture.read()
        if image_original is None:
            print('no more images captured')
            break
        #image_original = cv2.imread('/home/dabai/project/openpifpaf/images/14.png')#20190911151249.jpg')

        image = cv2.resize(image_original, None, fx=args.scale, fy=args.scale)
        print('resized image size: {}'.format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
        if visualizer is None:
            visualizer = Visualizer(processor, args)(image)
            visualizer.send(None)

        start = time.time()
        image_pil = PIL.Image.fromarray(image)
        processed_image_cpu, _, __ = transforms.EVAL_TRANSFORM(image_pil, [], None)
        processed_image = processed_image_cpu.contiguous().to(args.device, non_blocking=True)
        print('preprocessing time', time.time() - start)

        fields = processor.fields(torch.unsqueeze(processed_image, 0))[0]
        #print(fields[0],'keypoint?????')
        visualizer.send((image_original, fields))#image     image_original

        print('loop time = {:.3}s, FPS = {:.3}'.format(
            time.time() - last_loop, 1.0 / (time.time() - last_loop)))
        last_loop = time.time()


if __name__ == '__main__':
    main()
