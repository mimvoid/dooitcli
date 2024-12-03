{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  name = "dooit-parsing";

  packages = with pkgs; [
    python3
    dooit
  ];
}
