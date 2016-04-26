/**
* PostsController
* @namespace thinkster.posts.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.postsColumn.controllers')
    .controller('PostsColumnController', PostsColumnController);

  PostsColumnController.$inject = ['$scope'];

  /**
  * @namespace PostsController
  */
  function PostsColumnController($scope, $routeParams, Posts) {
    var vm = this;
    vm.posts = []
    activate();

    function activate(){
       var username = $routeParams.username.substr(1);
       Posts.get(username).then(postsSuccessFn, postsErrorFn);

      /**
      * @name postsSuccessFn
      * @desc Update posts array on view
      */
      function postsSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }

      /**
      * @name postsErrorFn
      * @desc Show snackbar with error
      */
      function postsErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }

    }

  }
})();