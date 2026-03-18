// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

import { OctantSignalForge } from "src/OctantSignalForge.sol";

contract Deploy is Script {
    function run() external returns (OctantSignalForge deployed) {
        address admin = vm.envAddress("ADMIN_WALLET_ADDRESS");
        address operator = vm.envAddress("OPERATOR_WALLET_ADDRESS");

        vm.startBroadcast();
        deployed = new OctantSignalForge(admin, operator);
        vm.stopBroadcast();

        console2.log("Deployed OctantSignalForge at", address(deployed));
    }
}
