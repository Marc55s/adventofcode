{
  description = "Advent of Code";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, treefmt-nix, rust-overlay }:
    let
      overlays = [ rust-overlay.overlays.default ];
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit overlays system;
      };
      rustVersion = pkgs.rust-bin.stable.latest.default;
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          rustVersion
          python311
          python311Packages.networkx
          python311Packages.matplotlib
          python311Packages.scipy
        ];
      };

      formatter.${system} = treefmt-nix.lib.mkWrapper
        nixpkgs.legacyPackages.${system}
        {
          projectRootFile = "flake.nix";
          programs.nixpkgs-fmt.enable = true;
          programs.rustfmt.enable = true;
        };
    };
}
