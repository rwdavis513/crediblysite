
/**
* NewPostController
* @namespace credibly.posts.controllers
*/
(function () {
  'use strict';

  angular
    .module('credibly.posts.controllers')
    .controller('NewPostController', NewPostController);

  NewPostController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Posts'];

  /**
  * @namespace NewPostController
  */
  function NewPostController($rootScope, $scope, Authentication, Snackbar, Posts) {
    var vm = this;

    vm.submit = submit;

    /**
    * @name submit
    * @desc Create a new Post
    * @memberOf credibly.posts.controllers.NewPostController
    */
    function submit() {
      //console.log("Submitting...")
      //var recipient = vm.recipient;
      //vm.recipient = recipient.toLowerCase();
      //console.log(vm.recipient.toLowerCase());
      /** Add username validation for recipient here */
      $rootScope.$broadcast('post.created', {
        content: vm.content,
        recipient: vm.recipient,
        relationship: vm.relationship,
        author: {
          username: Authentication.getAuthenticatedAccount().username
        }
      });

      $scope.closeThisDialog();

      Posts.create(vm.recipient,vm.content,vm.relationship).then(createPostSuccessFn, createPostErrorFn);


      /**
      * @name createPostSuccessFn
      * @desc Show snackbar with success message
      */
      function createPostSuccessFn(data, status, headers, config) {
        Snackbar.show('Success! Post created.');
      }


      /**
      * @name createPostErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPostErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('post.created.error');
        Snackbar.error(data.error);
      }
    }
  }
})();