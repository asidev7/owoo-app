import '/flutter_flow/flutter_flow_util.dart';
import 'mot_passe_oublie_widget.dart' show MotPasseOublieWidget;
import 'package:flutter/material.dart';

class MotPasseOublieModel extends FlutterFlowModel<MotPasseOublieWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // State field(s) for TextField widget.
  final textFieldKey = GlobalKey();
  FocusNode? textFieldFocusNode;
  TextEditingController? emailTextController;
  String? textFieldSelectedOption;
  String? Function(BuildContext, String?)? emailTextControllerValidator;

  /// Initialization and disposal methods.

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    textFieldFocusNode?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
