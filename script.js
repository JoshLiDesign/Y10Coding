var config = {
    apiKey: "AIzaSyDWOGt8QU-NfIYyDeBdTiCv7PuDeTHSw30",
    authDomain: "basic-9ddc3.firebaseapp.com",
    databaseURL: "https://basic-9ddc3.firebaseio.com",
    projectId: "basic-9ddc3",
    storageBucket: "basic-9ddc3.appspot.com",
    messagingSenderId: "528912636568",
    appId: "1:528912636568:web:9b7eb43652b72d34680eed",
    measurementId: "G-NYYM19W9WL"
};
firebase.initializeApp(config);

var loggedin;
var userId;
var display;


firebase.auth().onAuthStateChanged(function(user) {
    if (user == null) {
        userId = "Unknown"; //change this
        display = "Unknown"; //change this
        document.getElementById("login").innerHTML = "Log In";
        loggedin = false;
        document.getElementById("displayUsername").innerHTML = "Guest";
        document.getElementById("email").innerHTML = "";
        document.getElementById("photo").innerHTML = '<img class="circle" src="https://4.bp.blogspot.com/-H232JumEqSc/WFKY-6H-zdI/AAAAAAAAAEw/DcQaHyrxHi863t8YK4UWjYTBZ72lI0cNACLcB/s1600/profile%2Bpicture.png" id = "photo">'
        document.getElementById("publish").style.visibility = "hidden";
        document.getElementById("publish").disabled = true;
    } else {
        userId = user.uid;
        display = user.displayName;
        document.getElementById("login").innerHTML = "Log Out";
        loggedin = true;
        document.getElementById("login").disable = true;
        displayName = user.displayName;
        document.getElementById("displayUsername").innerHTML = displayName;
        emailId = user.email;
        document.getElementById("email").innerHTML = emailId;
        photoURL = user.photoURL;
        document.getElementById("photo").innerHTML = '<img class = "circle" src="' + photoURL + '">'
    } // end user null check
}); // end check auth state

function loginfunc() {
    if (loggedin == false) {
        var provider = new firebase.auth.GoogleAuthProvider();
    
        firebase.auth().signInWithRedirect(provider).then(function(result) { 
            window.location.replace("fbtest.html");
        });
        
        document.getElementById("login").disable = true;

        
    } 
    if (loggedin == true) {
        firebase.auth().signOut()
            .then(function() {
                // Sign-out successful.
            })
            .catch(function(error) {
                // An error happened
            });

    }
    
}

function publishpress() {
    if (loggedin == false) {
        
    }
    if (loggedin == true) {
        console.log("button pressed");
    }
}

