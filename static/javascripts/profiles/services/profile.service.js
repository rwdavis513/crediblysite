
/**
* Profile
* @namespace credibly.profiles.services
*/
(function () {
  'use strict';

  angular
    .module('credibly.profiles.services')
    .factory('Profile', Profile);

  Profile.$inject = ['$http'];

  /**
  * @namespace Profile
  */
  function Profile($http) {
    /**
    * @name Profile
    * @desc The factory to be returned
    * @memberOf credibly.profiles.services.Profile
    */
    var Profile = {
      destroy: destroy,
      get: get,
      update: update,
      getImage: getImage
    };

    return Profile;

    /////////////////////

    /**
    * @name destroy
    * @desc Destroys the given profile
    * @param {Object} profile The profile to be destroyed
    * @returns {Promise}
    * @memberOf credibly.profiles.services.Profile
    */
    function destroy(profile) {
      return $http.delete('/api/v1/accounts/' + profile.id + '/');
    }


    /**
    * @name get
    * @desc Gets the profile for user with username `username`
    * @param {string} username The username of the user to fetch
    * @returns {Promise}
    * @memberOf credibly.profiles.services.Profile
    */
    function get(username) {
      return $http.get('/api/v1/accounts/' + username + '/');

    }

    function getImage(userimageapi){
      //console.log(userimageapi);
      return $http.get(userimageapi);
    }
    /**
    * @name update
    * @desc Update the given profile
    * @param {Object} profile The profile to be updated
    * @returns {Promise}
    * @memberOf credibly.profiles.services.Profile
    */
    function update(profile) {
      return $http.put('/api/v1/accounts/' + profile.username + '/', profile);
    }
  }
})();
