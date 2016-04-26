
/**
* ProfileController
* @namespace credibly.profiles.controllers
*/
(function () {
  'use strict';

  angular
    .module('credibly.profiles.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Posts', 'Profile', 'Snackbar'];

  function ProfileController($location, $routeParams, Posts, Profile, Snackbar) {
    var vm = this;

    vm.profile = undefined;
    vm.posts = [];
    vm.isEmpty = isEmpty;

    activate();

    function activate() {
      //var username = $routeParams.username.substr(1);
      var username = $routeParams.username;
      /**console.log($routeParams)*/
      Profile.get(username).then(profileSuccessFn, profileErrorFn);
      Posts.get(username).then(postsSuccessFn, postsErrorFn);

      function profileSuccessFn(data, status, headers, config) {
        vm.profile = data.data;
        /**console.log("Vm.profile.address_city: ")
        console.log(vm.profile.address_city);
        console.log("---------------- ")
        */

        /**   Previous API had a separate call for the image url.
        if (vm.profile.image.url != '') {
          //console.log(vm.profile.image[1]);
          Profile.getImage(vm.profile.image.url).then(profileUserImageSuccessFn, profileUserImageErrorFn);
        }

        function profileUserImageSuccessFn(data, status, headers, config){
          vm.profile.userimage = data.data.image;
          console.log(vm.profile.userimage)
        }

        function profileUserImageErrorFn(data, status, headers, config) {
          Snackbar.error('UserImage not found.');
        }
        */
      }

      function profileErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That user does not exist.');
      }
      function postsSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
        /*console.log("-----");
        console.log(vm.posts[0].author.full_name);
        console.log("--------");
        console.log(vm.isEmpty(vm.posts[0].author.full_name));*/
      }
      function postsErrorFn(data, status, headers, config) {
        Snackbar.error(data.data.error);
      }
    }

    function isEmpty(obj) {
        var result = (obj == undefined | obj == '' | obj == null);
        return result;
    }
  }
})();