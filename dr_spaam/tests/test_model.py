import numpy as np
from dr_spaam.detector import Detector

ckpt = '/home/lfp/data/self_supervised_person_detection/ckpt_jrdb_ann_drow3_e40.pth'
detector = Detector(
    ckpt,
    model="DROW3",          # Or DR-SPAAM
    gpu=False,               # Use GPU
    stride=1,               # Optionally downsample scan for faster inference
    panoramic_scan=True     # Set to True if the scan covers 360 degree
)

# tell the detector field of view of the LiDAR
laser_fov_deg = 360
detector.set_laser_fov(laser_fov_deg)

# detection
num_pts = 1091
cnt = 0
while True:
    # create a random scan
    scan = np.random.rand(num_pts)  # (N,)

    # detect person
    dets_xy, dets_cls, instance_mask = detector(scan)  # (M, 2), (M,), (N,)

    # confidence threshold
    cls_thresh = 0.5
    cls_mask = dets_cls > cls_thresh
    dets_xy = dets_xy[cls_mask]
    dets_cls = dets_cls[cls_mask]
    print("prediced xy coord: {}, class: {}".format(dets_xy, dets_cls))

    if cnt > 30:
        break
    cnt += 1