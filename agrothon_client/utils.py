from gpiozero import MotionSensor, OutputDevice
from cv2 import VideoCapture, imencode
from .request_helper import *
import io
import logging
from serial import Serial
from agrothon_client import USB_PORT

serial_in = Serial(USB_PORT, 9600)

pump = OutputDevice(12, active_high=True, initial_value=True)

pir1 = MotionSensor(25)
pir2 = MotionSensor(8)
pir3 = MotionSensor(7)
pir4 = MotionSensor(1)

LOGGER = logging.getLogger(__name__)


def motion_intruder_detect():
    LOGGER.info("Starting Intruder Module")
    while True:
        if pir1.motion_detected or pir2.motion_detected or pir3.motion_detected or pir4.motion_detected:
            LOGGER.info(f"PIR1 : {pir1.value}, PIR2 : {pir2.value}, PIR3 : {pir3.value}. PIR4 : {pir4.value}")
            LOGGER.info("Launching camera")
            img_cap = VideoCapture(0)
            check, frame = img_cap.read()
            is_success, cv2_img = imencode(".jpg", frame)
            img_cap.release()
            if is_success:
                data = io.BytesIO(cv2_img)
                resp = image_poster(data)
                if resp:
                    LOGGER.info(f"Intruder Detected:{str(resp)}")
                else:
                    LOGGER.error("maybe nothing found")

def serial_sensor_in():
    LOGGER.info("Starting Sensor module")
    while True:
        if serial_in.in_waiting:
            serial_line = serial_in.readline().decode('utf-8').strip()
            list_of_values = serial_line.split(",")
            # sensor_data = []
            try:
                sensor_dict = {"moisture": float(list_of_values[0]),"humidity": float(list_of_values[2]), "temperature":float(list_of_values[1])}
                # for i in range(len(list_of_values)):
                #     sensor_dict[sensor_data[i]] = float(list_of_values[i])
                sensor_data_post(json=sensor_dict)
                # time.sleep(5)
            except ValueError:
                LOGGER.error(serial_line)
                LOGGER.error("DHT Data read failed")
                pass

def pump_status():
    LOGGER.info("Starting Pump status Check")
    while True:
        resp = pump_status_check()
        if resp:
            pump.off()

            LOGGER.info(f"Pump is {pump.value}")
        elif not resp:
            pump.on()
            LOGGER.info(f"Pump is {pump.value}")
        else:
            LOGGER.error("Bruhhhh....")
            pass
