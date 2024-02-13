#!/usr/bin/env python3
#Server to ROS
import socket
import rospy
from std_msgs.msg import String
from detection_msgs.msg import BoundingBox
from detection_msgs.msg import BoundingBoxes

if __name__ == '__main__':
    rospy.init_node('udp_server')
    localIP     = "127.0.0.1"
    localPort   = 20002
    bufferSize  = 1024

    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))

    # Publish the message to the topic
    pub = rospy.Publisher('detection_boxes', BoundingBoxes, queue_size=1)

    print("UDP server up and listening")

    while not rospy.is_shutdown():
        #Send message to rostopic
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        dictionary = eval(message)
        print(dictionary)
        boxes = BoundingBoxes()
        for key in dictionary:
            box = BoundingBox()
            box.probability = dictionary[key]['probability']
            box.xmin = dictionary[key]['xmin']
            box.xmax = dictionary[key]['xmax']
            box.ymin = dictionary[key]['ymin']
            box.ymax = dictionary[key]['ymax']
            box.Class = dictionary[key]['Class']
            box.xmin_coord = dictionary[key]['xmin_coord']
            box.ymin_coord = dictionary[key]['ymin_coord'] 
            boxes.bounding_boxes.append(box)
        pub.publish(boxes)