var AnnounceControllers = angular.module('AnnounceControllers', []);


AnnounceControllers.controller('AnnounceListCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.announceList = {};
    $scope.announcements = [];
    $scope.channel = 'announce';

    $dragon.onReady(function() {
        $dragon.subscribe('announcements', $scope.channel, {announce_list__id: 1}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });

        $dragon.getSingle('announce-list', {id:1}).then(function(response) {
            $scope.announceList = response.data;
        });

        $dragon.getList('announcements', {list_id:1}).then(function(response) {
            $scope.announcements = response.data;
        });
    });

    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper.mapData($scope.announcements, message);
            });
        }
    });
}]);
