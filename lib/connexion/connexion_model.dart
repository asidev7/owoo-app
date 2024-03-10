import '/flutter_flow/flutter_flow_util.dart';
import 'connexion_widget.dart' show ConnexionWidget;
import 'package:flutter/material.dart';

class ConnexionModel extends FlutterFlowModel<ConnexionWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // State field(s) for TextField widget.
  final textFieldKey1 = GlobalKey();
  FocusNode? textFieldFocusNode1;
  TextEditingController? emailTextController;
  String? textFieldSelectedOption1;
  String? Function(BuildContext, String?)? emailTextControllerValidator;
  // State field(s) for TextField widget.
  final textFieldKey2 = GlobalKey();
  FocusNode? textFieldFocusNode2;
  TextEditingController? passwordTextController;
  String? textFieldSelectedOption2;
  late bool passwordVisibility;
  String? Function(BuildContext, String?)? passwordTextControllerValidator;

  /// Initialization and disposal methods.

  @override
  void initState(BuildContext context) {
    passwordVisibility = false;
  }

  @override
  void dispose() {
    unfocusNode.dispose();
    textFieldFocusNode1?.dispose();

    textFieldFocusNode2?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
