from __future__ import division
#from ast import Str
#from asyncio import QueueEmpty
import os
import rospy
import rospkg
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler
from std_msgs.msg import String

from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt, Slot, Signal
from python_qt_binding.QtWidgets import QMainWindow, QMenu, QWidget
from python_qt_binding.QtGui import QIcon

class HuskyPandaWidget(QMainWindow):
      def __init__(self, context):
            super(HuskyPandaWidget, self).__init__()
            # Get path to UI file which should be in the "resource" folder of this package
            ui_file = os.path.join(rospkg.RosPack().get_path('rqt_dyros'), 'resource', 'HuskyPanda.ui')
            # Extend the widget with all attributes and children from UI file
            loadUi(ui_file, self, {'HuskyPandaWidget': HuskyPandaWidget})
            # Give QObjects reasonable names
            self.setObjectName('HuskyPanda')
            
            # ROS Variables
            self.publisher = None
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            self.roll = 0.0
            self.pitch = 0.0
            self.yaw = 0.0

            # Push Button
            self.open_push_button.pressed.connect(self.open_push_button_pressed)
            self.stop_push_button.pressed.connect(self.stop_push_button_pressed)
            self.reach_push_button.pressed.connect(self.reach_push_button_pressed)

            # Double Spin Box
            self.x_double_spin_box.setMinimum(-100.0)
            self.x_double_spin_box.setMaximum(100.0)
            self.y_double_spin_box.setMinimum(-100.0)
            self.y_double_spin_box.setMaximum(100.0)
            self.z_double_spin_box.setMinimum(-100.0)
            self.z_double_spin_box.setMaximum(100.0)
            self.roll_double_spin_box.setMinimum(-100.0)
            self.roll_double_spin_box.setMaximum(100.0)
            self.pitch_double_spin_box.setMinimum(-100.0)
            self.pitch_double_spin_box.setMaximum(100.0)
            self.yaw_double_spin_box.setMinimum(-100.0)
            self.yaw_double_spin_box.setMaximum(100.0)
            self.x_double_spin_box.valueChanged.connect(self.x_double_spin_box_changed)
            self.y_double_spin_box.valueChanged.connect(self.y_double_spin_box_changed)
            self.z_double_spin_box.valueChanged.connect(self.z_double_spin_box_changed)
            self.roll_double_spin_box.valueChanged.connect(self.roll_double_spin_box_changed)
            self.pitch_double_spin_box.valueChanged.connect(self.pitch_double_spin_box_changed)
            self.yaw_double_spin_box.valueChanged.connect(self.yaw_double_spin_box_changed)

      @Slot()
      def open_push_button_pressed(self):
            msg = String()
            msg = 'Open!'
            rospy.loginfo('Publish a message: {0}'.format(msg))
            self.publisher = rospy.Publisher('/open_push_button_pressed', String, queue_size=10)
            self.publisher.publish(msg)

      @Slot()
      def stop_push_button_pressed(self):
            msg = String()
            msg = 'Stop!'
            rospy.loginfo('Publish a message: {0}'.format(msg))
            self.publisher = rospy.Publisher('/stop_push_button_pressed', String, queue_size=10)
            self.publisher.publish(msg)

      @Slot()
      def reach_push_button_pressed(self):
            msg = Pose()
            msg.position.x = self.x
            msg.position.y = self.y
            msg.position.z = self.z
            msg.orientation = quaternion_from_euler(self.roll, self.pitch, self.yaw, 'sxyz')
            
            rospy.loginfo('Publish a message: {0}'.format(msg))
            self.publisher = rospy.Publisher('/reach_push_button_pressed', Pose, queue_size=10)
            self.publisher.publish(msg)

      def x_double_spin_box_changed(self, value):
            self.x = value

      def y_double_spin_box_changed(self, value):
            self.y = value
      
      def z_double_spin_box_changed(self, value):
            self.z = value

      def roll_double_spin_box_changed(self, value):
            self.roll = value

      def pitch_double_spin_box_changed(self, value):
            self.pitch = value
      
      def yaw_double_spin_box_changed(self, value):
            self.yaw = value

      def unregister_publisher(self):
            if self.publisher is not None:
                  self.publisher.unregister()
                  self.publisher = None

      def shutdown_all(self):
            self.unregister_publisher()