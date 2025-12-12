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
      pkgs = import nixpkgs { inherit overlays system; };
      rustVersion = pkgs.rust-bin.stable.latest.default;
      
      llvm = pkgs.llvmPackages; 
    in {
      devShells.${system}.default = pkgs.mkShell {
        
        # --- STATIC ENV VARIABLES ---
        Z3_SYS_Z3_HEADER = "${pkgs.lib.getDev pkgs.z3}/include/z3.h";
        Z3_LIBRARY_PATH_OVERRIDE = "${pkgs.lib.getLib pkgs.z3}/lib";
        LIBCLANG_PATH = "${llvm.libclang.lib}/lib";

        # --- DYNAMIC ENV VARIABLES (The Fix) ---
        # We use shellHook so we can run the clang command to find the header path.
        shellHook = ''
          export BINDGEN_EXTRA_CLANG_ARGS="$(echo \
            -I${pkgs.lib.getDev pkgs.z3}/include \
            -I${pkgs.lib.getDev pkgs.glibc}/include \
            -I$(${llvm.clang}/bin/clang -print-resource-dir)/include \
          )"
        '';

        buildInputs = [ pkgs.z3 llvm.libclang ];

        nativeBuildInputs = with pkgs; [
          pkg-config
          llvm.libclang
          llvm.clang
          rustVersion
          bacon
          python311
          python311Packages.networkx
          python311Packages.matplotlib
          python311Packages.scipy
        ];
      };

      formatter.${system} =
        treefmt-nix.lib.mkWrapper nixpkgs.legacyPackages.${system} {
          projectRootFile = "flake.nix";
          programs.nixpkgs-fmt.enable = true;
          programs.rustfmt.enable = true;
        };
    };
}
