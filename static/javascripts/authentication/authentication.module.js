(function() {
   'use strict';

   angular
      .module('credibly.authentication', [
          'credibly.authentication.controllers',
          'credibly.authentication.services'
      ]);

   angular
      .module('credibly.authentication.controllers', []);
   

   angular
      .module('credibly.authentication.services', ['ngCookies']);
})();     
