/**
* Register Controller
*/

(function () {
    'use strict';
    angular
       .module('credibly.authentication.controllers')
       .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    function RegisterController($location, $scope, Authentication) {
        var vm = this;
       
        vm.register = register;

        activate();
        function register() {
           Authentication.register(vm.email, vm.password, vm.username);
        }

        function activate(){
            if (Authentication.isAuthenticated()){
                $location.url('/');
            }
        }
     }
})();
 
