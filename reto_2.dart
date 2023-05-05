import 'dart:math';


void main() {
  List<int> arreglo = [];
  int n = Random().nextInt(20)+10;
  for (int i =0; i<n ; i++){
    arreglo.add(Random().nextInt(10));
  }
  print("$arreglo");
  arreglo.sort();
  print("arreglo ordendo $arreglo");
  arreglo.shuffle();
  print("arreglo desodernado aleatorio $arreglo");
  
}

