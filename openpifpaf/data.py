
'''COCO_PERSON_SKELETON = [
    [16, 14], [14, 12], [17, 15], [15, 13], [12, 13], [6, 12], [7, 13],
    [6, 7], [6, 8], [7, 9], [8, 10], [9, 11], [2, 3], [1, 2], [1, 3],
    [2, 4], [3, 5], [4, 6], [5, 7]]'''
COCO_PERSON_SKELETON = [
    [14, 13], [13, 12], [11, 10], [10, 9], [12, 8], [5, 12], [2, 9],
    [2, 5], [5, 6], [2, 3], [6, 7], [3, 4], [8, 9], [1, 16], [1, 15],
    [16, 18], [15, 17], [18, 5], [17, 2],
     [14,19],[19,20],[14,21],[11,22],[22,23],[11,24],[8,9]]

'''KINEMATIC_TREE_SKELETON = [
    (1, 2), (2, 4),  # left head
    (1, 3), (3, 5),
    (1, 6),
    (6, 8), (8, 10),  # left arm
    (1, 7),
    (7, 9), (9, 11),  # right arm
    (6, 12), (12, 14), (14, 16),  # left side
    (7, 13), (13, 15), (15, 17),
]'''
KINEMATIC_TREE_SKELETON = [
    (1, 16), (16, 18),(1,15),(15,17),
    (1, 5), (5, 6),(6,7),
    (1, 2),(2,3),(3,4),
    (5, 12), (12, 13),(13,14),  # left arm
    (2, 9),(9,10),(10,11),
    (14, 19), (19, 20),  # right arm
    (14, 21), (11, 22), (22, 23),(11,24),  # left side
    (8, 9), (8, 12),
]


'''COCO_KEYPOINTS = [
    'nose',            # 1
    'left_eye',        # 2
    'right_eye',       # 3
    'left_ear',        # 4
    'right_ear',       # 5
    'left_shoulder',   # 6
    'right_shoulder',  # 7
    'left_elbow',      # 8
    'right_elbow',     # 9
    'left_wrist',      # 10
    'right_wrist',     # 11
    'left_hip',        # 12
    'right_hip',       # 13
    'left_knee',       # 14
    'right_knee',      # 15
    'left_ankle',      # 16
    'right_ankle',     # 17
]'''
COCO_KEYPOINTS = [
    'nose',
    'right_shoulder',
    'right_elbow',
    'right_wrist',
    'left_shoulder',
    'left_elbow',
    'left_wrist',
    'hip',
    'right_hip',
    'right_knee',
    'right_ankle',
    'left_hip',
    'left_knee',
    'left_ankle',
    'right_eye',
    'left_eye',
    'right_ear',
    'left_ear',

    'left_foot19',
    'left_foot20',
    'left_heel',
    'right_foot22',
    'right_foot23',
    'right_heel',
]


HFLIP = {
    'left_eye': 'right_eye',
    'right_eye': 'left_eye',
    'left_ear': 'right_ear',
    'right_ear': 'left_ear',
    'left_shoulder': 'right_shoulder',
    'right_shoulder': 'left_shoulder',
    'left_elbow': 'right_elbow',
    'right_elbow': 'left_elbow',
    'left_wrist': 'right_wrist',
    'right_wrist': 'left_wrist',
    'left_hip': 'right_hip',
    'right_hip': 'left_hip',
    'left_knee': 'right_knee',
    'right_knee': 'left_knee',
    'left_ankle': 'right_ankle',
    'right_ankle': 'left_ankle',

    'left_foot19':'right_foot22',
     'right_foot22':'left_foot19',
    'left_foot20':'right_foot23',
    'right_foot23':'left_foot20',
    'left_heel':'right_heel',
    'right_heel': 'left_heel',
}


'''DENSER_COCO_PERSON_SKELETON = [
    (1, 2), (1, 3), (2, 3), (1, 4), (1, 5), (4, 5),
    (1, 6), (1, 7), (2, 6), (3, 7),
    (2, 4), (3, 5), (4, 6), (5, 7), (6, 7),
    (6, 12), (7, 13), (6, 13), (7, 12), (12, 13),
    (6, 8), (7, 9), (8, 10), (9, 11), (6, 10), (7, 11),
    (8, 9), (10, 11),
    (10, 12), (11, 13),
    (10, 14), (11, 15),
    (14, 12), (15, 13), (12, 15), (13, 14),
    (12, 16), (13, 17),
    (16, 14), (17, 15), (14, 17), (15, 16),
    (14, 15), (16, 17),
]'''
DENSER_COCO_PERSON_SKELETON = [
    (1, 16), (1, 15), (15, 16), (1, 18), (1, 17), (18, 17),
    (1, 5), (1, 2), (16, 5), (15, 2),
    (16, 18), (15, 17), (18, 5), (17, 2), (2, 5),
    (5, 12), (2, 9), (5, 9), (2, 12), (12, 9),
    (5, 6), (2, 3), (6, 7), (3, 4), (5, 7), (2, 4),
    (6, 3), (7, 4),
    (7, 12), (4, 9),
    (7, 13), (4, 10),
    (12, 13), (9, 10), (12, 10), (9, 13),
    (12, 14), (9, 11),
    (14, 13), (11, 10), (13, 11), (10, 14),
    (10, 13), (14, 11),

    (14,19),(11,22),(19,20),(22,23),(14,21),(11,24),
    (14,20),(11,23),(20,12),(23,9),(21,8),(24,8),(8,12),(8,9)
]

'''COCO_PERSON_SIGMAS = [
    0.026,  # nose
    0.025,  # eyes
    0.025,  # eyes
    0.035,  # ears
    0.035,  # ears
    0.079,  # shoulders
    0.079,  # shoulders
    0.072,  # elbows
    0.072,  # elbows
    0.062,  # wrists
    0.062,  # wrists
    0.107,  # hips
    0.107,  # hips
    0.087,  # knees
    0.087,  # knees
    0.089,  # ankles
    0.089,  # ankles
]'''


COCO_PERSON_SIGMAS = [
    0.026,  # nose
    0.025,  # eyes
    0.025,  # eyes
    0.035,  # ears
    0.035,  # ears
    0.079,  # shoulders
    0.079,  # shoulders
    0.072,  # elbows
    0.072,  # elbows
    0.062,  # wrists
    0.062,  # wrists
    0.107,  # hips
    0.107,  # hips
    0.087,  # knees
    0.087,  # knees
    0.089,  # ankles
    0.089,  # ankles
    0.089,
    0.089,
    0.089,
    0.089,
    0.089,
    0.089,
    0.089,
]


def draw_skeletons():
    import numpy as np
    from . import show
    coordinates = np.array([[
        [0.0, 9.3, 2.0],  # 'nose',            # 1
        [-0.5, 9.7, 2.0],  # 'left_eye',        # 2
        [0.5, 9.7, 2.0],  # 'right_eye',       # 3
        [-1.0, 9.5, 2.0],  # 'left_ear',        # 4
        [1.0, 9.5, 2.0],  # 'right_ear',       # 5
        [-2.0, 8.0, 2.0],  # 'left_shoulder',   # 6
        [2.0, 8.0, 2.0],  # 'right_shoulder',  # 7
        [-2.5, 6.0, 2.0],  # 'left_elbow',      # 8
        [2.5, 6.2, 2.0],  # 'right_elbow',     # 9
        [-2.5, 4.0, 2.0],  # 'left_wrist',      # 10
        [2.5, 4.2, 2.0],  # 'right_wrist',     # 11
        [-1.8, 4.0, 2.0],  # 'left_hip',        # 12
        [1.8, 4.0, 2.0],  # 'right_hip',       # 13
        [-2.0, 2.0, 2.0],  # 'left_knee',       # 14
        [2.0, 2.1, 2.0],  # 'right_knee',      # 15
        [-2.0, 0.0, 2.0],  # 'left_ankle',      # 16
        [2.0, 1.1, 2.0],  # 'right_ankle',     # 17

        [-2.0, 0.3, 2.0],
        [-0.2, 3.5, 2.0],
        [0.0, 0.7, 2.0],
        [2.0, 5.9, 2.0],
        [-1.0, 0.9, 2.0],
        [1.0, 2.1, 2.0],
        [1.0, 7.1, 2.0],
    ]])

    keypoint_painter = show.KeypointPainter(show_box=False, color_connections=True,
                                            markersize=1, linewidth=6)

    with show.canvas('docs/skeleton_coco.png', figsize=(2, 5)) as ax:
        ax.set_axis_off()
        keypoint_painter.skeleton = COCO_PERSON_SKELETON
        keypoint_painter.keypoints(ax, coordinates)

    with show.canvas('docs/skeleton_kinematic_tree.png', figsize=(2, 5)) as ax:
        ax.set_axis_off()
        keypoint_painter.skeleton = KINEMATIC_TREE_SKELETON
        keypoint_painter.keypoints(ax, coordinates)

    with show.canvas('docs/skeleton_dense.png', figsize=(2, 5)) as ax:
        ax.set_axis_off()
        keypoint_painter.skeleton = DENSER_COCO_PERSON_SKELETON
        keypoint_painter.keypoints(ax, coordinates)


def print_associations():
    for j1, j2 in COCO_PERSON_SKELETON:
        print(COCO_KEYPOINTS[j1 - 1], '-', COCO_KEYPOINTS[j2 - 1])


if __name__ == '__main__':
    print_associations()
    draw_skeletons()
