(function () {
   'use strict';

   angular
     .module('credibly', [
         'credibly.config',
         'credibly.routes',
         'credibly.authentication',
         'credibly.layout',
         'credibly.posts',
         'credibly.utils',
         'credibly.profiles'
     ]);

   angular
      .module('credibly.routes',['ngRoute']);

   angular
      .module('credibly.config', []);
  
   angular
      .module('credibly')
      .run(run);


   run.$inject = ['$http'];

   function run($http) {
      $http.defaults.xsrfHeaderName = 'X-CSRFToken';
      $http.defaults.xsrfCookieName = 'csrftoken';
   }

})();

