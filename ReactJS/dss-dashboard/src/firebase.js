import firebase from 'firebase';
const config = {
	apiKey: "AIzaSyDvsvuPnCfyX3Ol2EKCPRb_Y72eOEedZUE",
	authDomain: "the-dss.firebaseapp.com",
	databaseURL: "https://the-dss.firebaseio.com",
	projectId: "the-dss",
	storageBucket: "the-dss.appspot.com",
	messagingSenderId: "520356870365",
	appId: "1:520356870365:web:7076d5893b797c3fb00334",
	measurementId: "G-399MXR9YNY"
};
firebase.initializeApp(config);
// const db = firebaseApp.firestore();

// export{ db }
export default firebase
