import cv2
from ultralytics import YOLO
import supervision as sv
import numpy as np
import argparse
import time



import webbrowser

def open_html_file():
    
    html_file_path = 'D:\PROJECT SOURCE CODE AND FILES\manager.html'
    webbrowser.open(html_file_path)



LINE_START = sv.Point(320, 0)
LINE_END = sv.Point(320, 480)

ZONE_POLYGON = np.array([
    [0, 0],
    [0.25, 0],
    [0.25, 1],
    [0, 1]
])




def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="yolo")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280, 720], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args

def main():


    tim=0
    args = parse_arguments()
    line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
    line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
    )

    model = YOLO("items.pt")
    for result in model.track(source=0, show=True, stream=True, agnostic_nms=True):
        
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        
        detections = detections[(detections.class_id != 60) & (detections.class_id != 0)]

        

        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections,
            
        )

        zone_polygon = (ZONE_POLYGON * np.array(args.webcam_resolution)).astype(int)
        zone = sv.PolygonZone(polygon=zone_polygon, frame_resolution_wh=tuple(args.webcam_resolution))
        zone_annotator = sv.PolygonZoneAnnotator(
        zone=zone, 
        color=sv.Color.red(),
        thickness=2,
        text_thickness=4,
        text_scale=2
        )


        line_counter.trigger(detections=detections)
        
        print(f"{model.model.names[class_id] } "for class_id in detections)
        zone.trigger(detections=detections)
        
        start_time = time.time()
        

        if(zone.current_count == 0):
            tim=tim+1
            print(tim)
            if tim == 10 :
                open_html_file()
                print("item out of stock")
        else:
            tim = 0
            

        
        
        frame = zone_annotator.annotate(scene=frame)

        cv2.imshow("yolov8", frame)

        


if __name__ == "__main__":
    main()