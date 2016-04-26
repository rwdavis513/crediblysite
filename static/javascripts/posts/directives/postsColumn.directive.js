/**
* Posts
* @namespace credibly.posts.directives
*/
(function () {
  'use strict';

  angular
    .module('credibly.posts.directives')
    .directive('postsColumn', posts);

  /**
  * @namespace Posts
  */
  function posts() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf credibly.posts.directives.Posts
    */
    var directive = {
      controller: 'PostsColumnController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        posts: '='
      },
      templateUrl: '/static/templates/posts/postsColumn.html'
    };

    return directive;
  }
})();