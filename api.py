import os
import time
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


###
# Define endpoint actions.
###

class Dock(Resource):
    def get(self):
        os.system('sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 action send_goal /dock irobot_create_msgs/action/Dock "{}"')
        return None

class UnDock(Resource):
    def get(self):
        os.system('sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 action send_goal /undock irobot_create_msgs/action/Undock "{}"')
        return None

class Up(Resource):
    def get(self):
        os.system("sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance \"{distance: 1.0,max_translation_speed: 0.15}\"")
        return None

class Down(Resource):
    def get(self):
        os.system("sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance \"{distance: -1.0,max_translation_speed: 0.15}\"")
        time.sleep(1)
        return None

class Left(Resource):
    def get(self):
        os.system("sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle \"{angle: 1.57,max_rotation_speed: 0.5}\"")
        return None
    
class Right(Resource):
    def get(self):
        os.system("sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle \"{angle: -1.57,max_rotation_speed: 0.5}\"")
        return None
    

###
# Attach endpoints.
###

api.add_resource(Dock, '/dock')
api.add_resource(UnDock, '/undock')
api.add_resource(Up, '/up')
api.add_resource(Down, '/down')
api.add_resource(Left, '/left')
api.add_resource(Right, '/right')

# Live dangerously.
os.system("sudo docker run -d --rm --network=host --privileged -e DISPLAY=$DISPLAY irobotedu/create3-humble:0.0.1 ros2 param set /motion_control safety_override full")

###
# Start server.
###

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
