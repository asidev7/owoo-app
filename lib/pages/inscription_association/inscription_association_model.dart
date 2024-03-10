import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/form_field_controller.dart';
import 'inscription_association_widget.dart' show InscriptionAssociationWidget;
import 'package:flutter/material.dart';

class InscriptionAssociationModel
    extends FlutterFlowModel<InscriptionAssociationWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // State field(s) for RadioButton widget.
  FormFieldController<String>? radioButtonValueController;
  // State field(s) for TextField widget.
  final textFieldKey1 = GlobalKey();
  FocusNode? textFieldFocusNode1;
  TextEditingController? textController1;
  String? textFieldSelectedOption1;
  String? Function(BuildContext, String?)? textController1Validator;
  // State field(s) for TextField widget.
  final textFieldKey2 = GlobalKey();
  FocusNode? textFieldFocusNode2;
  TextEditingController? textController2;
  String? textFieldSelectedOption2;
  String? Function(BuildContext, String?)? textController2Validator;
  // State field(s) for TextField widget.
  final textFieldKey3 = GlobalKey();
  FocusNode? textFieldFocusNode3;
  TextEditingController? textController3;
  String? textFieldSelectedOption3;
  String? Function(BuildContext, String?)? textController3Validator;
  // State field(s) for TextField widget.
  final textFieldKey4 = GlobalKey();
  FocusNode? textFieldFocusNode4;
  TextEditingController? textController4;
  String? textFieldSelectedOption4;
  String? Function(BuildContext, String?)? textController4Validator;
  // State field(s) for TextField widget.
  final textFieldKey5 = GlobalKey();
  FocusNode? textFieldFocusNode5;
  TextEditingController? textController5;
  String? textFieldSelectedOption5;
  late bool passwordVisibility1;
  String? Function(BuildContext, String?)? textController5Validator;
  // State field(s) for TextField widget.
  final textFieldKey6 = GlobalKey();
  FocusNode? textFieldFocusNode6;
  TextEditingController? textController6;
  String? textFieldSelectedOption6;
  late bool passwordVisibility2;
  String? Function(BuildContext, String?)? textController6Validator;

  /// Initialization and disposal methods.

  @override
  void initState(BuildContext context) {
    passwordVisibility1 = false;
    passwordVisibility2 = false;
  }

  @override
  void dispose() {
    unfocusNode.dispose();
    textFieldFocusNode1?.dispose();

    textFieldFocusNode2?.dispose();

    textFieldFocusNode3?.dispose();

    textFieldFocusNode4?.dispose();

    textFieldFocusNode5?.dispose();

    textFieldFocusNode6?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.

  String? get radioButtonValue => radioButtonValueController?.value;
}
