<launch>
  <include file="$(find pimouse_ros)/scripts/pimouse.launch" /> 
  <node pkg="pimouse_run_corridor" name="wall_stop_accel" type="wall_stop_accel.py" required="true" />
  <test test-name="test_wall_stop" pkg="pimouse_run_corridor" type="travis_test_wall_stop.py" />
</launch>
