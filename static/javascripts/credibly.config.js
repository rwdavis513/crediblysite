(function () {
   angular
      .module('credibly.config')
      .config(config);

   config.$inject = ['$locationProvider'];

   function config($locationProvider) {
      $locationProvider.html5Mode(true);
      $locationProvider.hashPrefix('!');
   }
})();

