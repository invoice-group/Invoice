app.service("service", ["$http", function($http) {
  this.do_save_info = function(username, password, callback) {
    $http({
      method: 'POST',
      url: '/do_save_info',
      data: {
        'username': username,
        'password': password
      },
      headers: {'Content-Type': undefined},
    }).success(function(response){
      callback(response);
    });
  };
}]);