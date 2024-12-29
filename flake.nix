{
  description = "Flake for dooit_scripts";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    dooit.url = "github:dooit-org/dooit";
  };

  outputs = { self, nixpkgs, ... } @ inputs:
    let
      allSystems = nixpkgs.lib.genAttrs nixpkgs.lib.platforms.all;

      toSystems = passPkgs: allSystems (system:
        passPkgs (import nixpkgs { inherit system;  })
      );
    in
    {
      devShells = toSystems (pkgs: {
        default = pkgs.mkShell {
          name = "dooit_scripts";

          packages =
            let
              python = pkgs.python312.withPackages (
                ps: with ps; [
                  dateutil
                  rich
                  sqlalchemy
                ]
              );
            in
            [
              python
              inputs.dooit.packages.${pkgs.system}.default
            ];
        };
      });
    };
}
