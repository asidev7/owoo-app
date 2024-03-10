import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: const FirebaseOptions(
            apiKey: "AIzaSyAdjZn3wXIbkir0SgggoYRC9eElI7wwhhE",
            authDomain: "owoo-1d3ed.firebaseapp.com",
            projectId: "owoo-1d3ed",
            storageBucket: "owoo-1d3ed.appspot.com",
            messagingSenderId: "533683874980",
            appId: "1:533683874980:web:49779f7cb8894919378a31"));
  } else {
    await Firebase.initializeApp();
  }
}
