var app = angular.module("myApp", []);
app.config(
  function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  })
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
app.controller("myCtrl", ["$scope", "service", function($scope, service) {
  $scope.result = "";
  $scope.my_submit = function() {
    console.log($scope.username);
    console.log($scope.password);
    service.do_save_info($scope.username, $scope.password, function(response){
      console.log(response);
      $scope.result = response.result;
    });
  };
}]); 