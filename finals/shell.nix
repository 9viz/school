with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "py-school-environment";

  buildInputs = with pkgs; [ python37 ]
            ++ (with pkgs.python37Packages; [ numpy matplotlib ]);
}
