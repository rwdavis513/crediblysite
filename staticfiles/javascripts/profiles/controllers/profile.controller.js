
/**
* ProfileController
* @namespace thinkster.profiles.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.profiles.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Posts', 'Profile', 'Snackbar'];

  /**
  * @namespace ProfileController
  */
  function ProfileController($location, $routeParams, Posts, Profile, Snackbar) {
    var vm = this;

    vm.profile = undefined;
    vm.posts = [];
    vm.isEmpty = isEmpty;
    //vm.userimage = undefined;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.profiles.controllers.ProfileController
    */
    function activate() {
      var username = $routeParams.username.substr(1);
      /**console.log($routeParams)*/
      Profile.get(username).then(profileSuccessFn, profileErrorFn);
      Posts.get(username).then(postsSuccessFn, postsErrorFn);

      /**
      * @name profileSuccessProfile
      * @desc Update `profile` on viewmodel
      */
      function profileSuccessFn(data, status, headers, config) {
        vm.profile = data.data;
        console.log(isEmpty(vm.profile.image[0]));
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



      /**
      * @name profileErrorFn
      * @desc Redirect to index and show error Snackbar
      */
      function profileErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That user does not exist.');
      }


      /**
        * @name postsSucessFn
        * @desc Update `posts` on viewmodel
        */
      function postsSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }


      /**
        * @name postsErrorFn
        * @desc Show error snackbar
        */
      function postsErrorFn(data, status, headers, config) {
        Snackbar.error(data.data.error);
      }
    }

    function isEmpty(obj) {
        return (obj == undefined);
    }
  }
})();