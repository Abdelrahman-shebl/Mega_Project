// // var ros;
// // var buttonsService; // Global variable for the service

// // function Init() {
// //     Joystick();
// // }

// // function Connect() {
  
//   //     ros.on('connection', () => {
//     //         console.log('Connected to ROS Bridge');
    
//     //         // Update the global variable with the reference to the service
//     //         buttonsService = new ROSLIB.Service({
// //             ros: ros,
// //             name: '/Buttons',
// //             serviceType: 'GUI/Buttons'
// //         });

// //         document.getElementById("Start").disabled = true;
// //         document.getElementById("Status-ros").textContent = "Connected";
// //         document.getElementById("Status-ros").classList.remove("badge", "bg-danger");
// //         document.getElementById("Status-ros").classList.add("badge", "bg-success");
// //     });

// //     ros.on('error', (error) => {
// //         console.error('Error connecting to ROS Bridge:', error);
// //     });

// //     ros.on('close', () => {
//   //         console.log('Disconnected from ROS Bridge');
//   //         document.getElementById("Start").disabled = false;
// //         document.getElementById("Status-ros").textContent = "Disconnected";
// //         document.getElementById("Status-ros").classList.remove("badge", "bg-success");
// //         document.getElementById("Status-ros").classList.add("badge", "bg-danger");
// //     });
// // }

// // function Joystick() {
//   //     window.addEventListener("gamepadconnected", function (e) {
//     //         console.log("Gamepad connected:", e.gamepad);
//     //         document.getElementById("Status-joy").textContent = "Connected";
//     //         document.getElementById("Status-joy").classList.remove("badge", "bg-danger");
// //         document.getElementById("Status-joy").classList.add("badge", "bg-primary");

// //         // Start listening for button presses
// //         setInterval(function () {
//   //             let gamepad = navigator.getGamepads()[0];
//   //             let y_axis = gamepad.axes[0];
//   //             let x_axis = gamepad.axes[1];
// //             let yaw = gamepad.axes[5];
// //             let z_axis = gamepad.axes[6];
// //             let pitch = gamepad.axes[9];
// //             checkGamepadButtons(gamepad);
// //             console.log(pitch);
// //         }, 150); // Interval
// //     });

// //     window.addEventListener("gamepaddisconnected", function (e) {
//   //         console.log("Gamepad disconnected:", e.gamepad);
//   //         document.getElementById("Start").disabled = false;
//   //         document.getElementById("Status-joy").textContent = "Disconnected";
//   //         document.getElementById("Status-joy").classList.remove("badge", "bg-success");
//   //         document.getElementById("Status-joy").classList.add("badge", "bg-danger");
//   //     });
//   // }
  
//   // function checkGamepadButtons(gamepad) {
//     //     if (gamepad) {
//       //         for (var i = 0; i < gamepad.buttons.length; i++) {
//         //             if (gamepad.buttons[i].pressed) {
// //                 console.log("Button " + i + " pressed");

// //                 var request = new ROSLIB.ServiceRequest({
//   //                     Index: i,
//   //                 });
  
//   //                 // Use the global variable to call the service
//   //                 buttonsService.callService(request, function (result) {
// //                     console.log('Result for service call on ' + buttonsService.name + ': ' + result.Received);
// //                 });
// //             }
// //         }
// //     }
// // }
// const host = 'ws://localhost:9090';

// ros = new ROSLIB.Ros({
//     url: host,
// });
// pid_status = new ROSLIB.Service({
//     ros: ros,
//     name: "/7amo",
//     serviceType: "GUI/Buttons"
//   });
//   var cmdVel = new ROSLIB.Topic({
//      ros : ros,
//      name : '/cmd_vel',
//      messageType : 'geometry_msgs/Twist'
//     });
    
//     var twist = new ROSLIB.Message({
//       linear : {
//         x : 0.1,
//         y : 0.2,
//         z : 0.3
//       },
//       angular : {
//         x : -0.1,
//        y : -0.2,
//        z : -0.3
//      }
//      });
//      cmdVel.publish(twist);
const host = 'ws://localhost:9090';

ros = new ROSLIB.Ros({
    url: host,
});

// Declare the service client
pid_status = new ROSLIB.Service({
    ros: ros,
    name: "/7amo",
    serviceType: "GUI/Buttons"
});

// Prepare a request for the service
var request = new ROSLIB.ServiceRequest({
    // Include any parameters needed by the service
    // Example: param1: value1,
});

// Make the service call
pid_status.callService(request, function(result) {
    console.log('Result for service call on ' + pid_status.name + ': ' + result.Received);
    // Process the result if needed
});