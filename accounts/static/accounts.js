/* global $ */

var initialize = function(navigator, user, token, urls) {
    $('#id_login').on('click', function() {
        navigator.id.request();
        // navigator.id.doSomethingElse();
    });
    
    navigator.id.watch({
        loggedInUser: user
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    } 
};
/*

function setUpModule() {
    window.Superlists = {
        Accounts: {
            initialize: initialize
        } 
    };
}
QUnit.module('tests',{beforeEach: setUpModule});

*/
