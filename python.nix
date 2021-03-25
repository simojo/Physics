{ pkgs ? import <unstable> {} }:

let
  shellname = "python";
  myPython = with pkgs; [
    python38Full
    python38Packages.numpy
    python38Packages.matplotlib
    python38Packages.pip
    python38Packages.pylint
  ];
in
  pkgs.stdenv.mkDerivation {
    name = shellname;
    buildInputs = [
      myPython
    ];
    shellHook = ''
      export NIX_SHELL_NAME='${shellname}'
      alias p='python3'
    '';
  }
