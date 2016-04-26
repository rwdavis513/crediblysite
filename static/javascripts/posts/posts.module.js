
(function () {
  'use strict';

  angular
    .module('credibly.posts', [
      'credibly.posts.controllers',
      'credibly.posts.directives',
      'credibly.posts.services'
    ]);

  angular
    .module('credibly.posts.controllers', []);

  angular
    .module('credibly.posts.directives', ['ngDialog']);

  angular
    .module('credibly.posts.services', []);
})();

