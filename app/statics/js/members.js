/******/ (function(modules) { // webpackBootstrap
/******/ 	// install a JSONP callback for chunk loading
/******/ 	function webpackJsonpCallback(data) {
/******/ 		var chunkIds = data[0];
/******/ 		var moreModules = data[1];
/******/ 		var executeModules = data[2];
/******/ 		// add "moreModules" to the modules object,
/******/ 		// then flag all "chunkIds" as loaded and fire callback
/******/ 		var moduleId, chunkId, i = 0, resolves = [];
/******/ 		for(;i < chunkIds.length; i++) {
/******/ 			chunkId = chunkIds[i];
/******/ 			if(installedChunks[chunkId]) {
/******/ 				resolves.push(installedChunks[chunkId][0]);
/******/ 			}
/******/ 			installedChunks[chunkId] = 0;
/******/ 		}
/******/ 		for(moduleId in moreModules) {
/******/ 			if(Object.prototype.hasOwnProperty.call(moreModules, moduleId)) {
/******/ 				modules[moduleId] = moreModules[moduleId];
/******/ 			}
/******/ 		}
/******/ 		if(parentJsonpFunction) parentJsonpFunction(data);
/******/ 		while(resolves.length) {
/******/ 			resolves.shift()();
/******/ 		}
/******/
/******/ 		// add entry modules from loaded chunk to deferred list
/******/ 		deferredModules.push.apply(deferredModules, executeModules || []);
/******/
/******/ 		// run deferred modules when all chunks ready
/******/ 		return checkDeferredModules();
/******/ 	};
/******/ 	function checkDeferredModules() {
/******/ 		var result;
/******/ 		for(var i = 0; i < deferredModules.length; i++) {
/******/ 			var deferredModule = deferredModules[i];
/******/ 			var fulfilled = true;
/******/ 			for(var j = 1; j < deferredModule.length; j++) {
/******/ 				var depId = deferredModule[j];
/******/ 				if(installedChunks[depId] !== 0) fulfilled = false;
/******/ 			}
/******/ 			if(fulfilled) {
/******/ 				deferredModules.splice(i--, 1);
/******/ 				result = __webpack_require__(__webpack_require__.s = deferredModule[0]);
/******/ 			}
/******/ 		}
/******/ 		return result;
/******/ 	}
/******/
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// object to store loaded and loading chunks
/******/ 	// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 	// Promise = chunk loading, 0 = chunk loaded
/******/ 	var installedChunks = {
/******/ 		"members": 0
/******/ 	};
/******/
/******/ 	// script path function
/******/ 	function jsonpScriptSrc(chunkId) {
/******/ 		return __webpack_require__.p + "" + ({}[chunkId]||chunkId) + ".js"
/******/ 	}
/******/
/******/ 	var deferredModules = [];
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	var jsonpArray = window["webpackJsonp"] = window["webpackJsonp"] || [];
/******/ 	var oldJsonpFunction = jsonpArray.push.bind(jsonpArray);
/******/ 	jsonpArray.push = webpackJsonpCallback;
/******/ 	jsonpArray = jsonpArray.slice();
/******/ 	for(var i = 0; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]);
/******/ 	var parentJsonpFunction = oldJsonpFunction;
/******/
/******/
/******/ 	// add entry module to deferred list
/******/ 	deferredModules.push(["./src/js/members.js","vendor"]);
/******/ 	// run deferred modules when ready
/******/ 	return checkDeferredModules();
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/js/members.js":
/*!***************************!*\
  !*** ./src/js/members.js ***!
  \***************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var vue_i18n__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue-i18n */ "./node_modules/vue-i18n/dist/vue-i18n.esm.js");
var Vue = __webpack_require__(/*! vue */ "./node_modules/vue/dist/vue.common.js");
var VueRouter = __webpack_require__(/*! vue-router */ "./node_modules/vue-router/dist/vue-router.common.js");
Vue.use(VueRouter);

var locale = document.getElementsByTagName('html')[0].getAttribute('lang');

Vue.use(vue_i18n__WEBPACK_IMPORTED_MODULE_0__["default"]);
var messages = {
  ja: __webpack_require__(/*! ./translations/ja-message.json */ "./src/js/translations/ja-message.json"),
};
var i18n = new vue_i18n__WEBPACK_IMPORTED_MODULE_0__["default"]({
  locale: locale,
  fallbackLocale: 'en',
  messages
});

var moment = __webpack_require__(/*! moment */ "./node_modules/moment/moment.js");
__webpack_require__(/*! moment/locale/ja */ "./node_modules/moment/locale/ja.js");
moment.locale(locale);
////Vue.use(require('vue-moment'));
Vue.filter('moment', function (date) {
  return moment(date).format('LLL');
});

var Buefy = __webpack_require__(/*! buefy */ "./node_modules/buefy/lib/index.js");
//Vue.use(Buefy.default);
Vue.component(Buefy.default.Loading.name, Buefy.default.Loading);

// axios を require してインスタンスを生成する
const axiosBase = __webpack_require__(/*! axios */ "./node_modules/axios/index.js");
const axios = axiosBase.create({
  baseURL: '/',
  headers: {
    'ContentType': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': locale
  },
  responseType: 'json'
});

var uriPrefix = '/members';
var MemberList = {
  // HTML上のscriptタグのidを指定する
  template: '#member-list',
  delimiters: ['[[', ']]'],
  data: function() {
    return {
      isLoading: false,
      members: function() { return []; },// 初期値の空配列を定義
      error: null
    };
  },
  // 初期化時にデータを取得する
  created: function () {
    this.fetchData();
  },
  // ルーティング変更時に再度データ取得するために$routeの変更をwatch
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData: function () {
      this.isLoading = true;
      var uri = 'api/members';// 取得したデータの結果の格納
      var apiParams = {};
      axios.get(uri, {params: apiParams})
      .then(response => {
        console.log(response.data.items);
        this.members = response.data.items;
				this.isLoading = false;
      })
      .catch(function(error) {
        this.error = error.toString();
				this.isLoading = false;
      });
    }
  }
};

var Member = {
  delimiters: ['[[', ']]'],
  template: '#member-detail',
  data: function () {
    return {
      isLoading: false,
      member: function () { return {} },
      error: null
    }
  },
  // 初期化時にデータを取得する
  created: function () {
    this.fetchData()
  },
  // ルーティング変更時に再度データ取得するために$routeの変更をwatch
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData: function () {
      this.loading = true
      var uri = '/api/members/' + this.$route.params.memberId;// 取得したデータの結果の格納
      var apiParams = {};
      axios.get(uri, {params: apiParams})
      .then(response => {
        this.member = response.data;
        this.loading = false
      })
      .catch(function(error) {
        console.log(error);
        this.error = error.toString()
        this.loading = false
      });
    }
  }
}

// ユーザー詳細ページ内で部分的に表示されるユーザーのプロフィールページ
var MemberProfile = {
  delimiters: ['[[', ']]'],
  template:
    '<div class="member-profile">' + 
      '<h3>こちらはユーザー [[ $route.params.memberId ]] のプロフィールページです。</h3>' +
    '</div>'
}

// ユーザー詳細ページ内で部分的に表示されるユーザーの投稿ページ
var MemberPosts = {
  template:
    '<div class="member-posts">' + 
      '<h3>こちらはユーザー [[ $route.params.memberId ]] の投稿ページです。</h3>' +
    '</div>'
}

// NotFound
var NotFound = {
  template:
    '<div class="notfound">' + 
      '<h3>404: Not Found</h3>' +
    '</div>'
}

// ルートオプションを渡してルーターインスタンスを生成します
var router = new VueRouter({
  mode: 'history',
  saveScrollPosition: true,
  routes: [
    {
      path: '/',
      component: {
        template: '<div>トップページです。</div>'
      }
    },
    {
      path: uriPrefix + '/',
      component: MemberList
    },
    {
      path: uriPrefix + '/:memberId',
      component: Member,
      name: 'member',
      beforeEnter: (to, from, next) => {
        if (Number.isInteger(parseInt(to.params.memberId)) !== true) {
          next('/members')
        } else {
          next()
        }
      }
    },
//    {
//      path: uriPrefix + '/me',
//      component: {
//        template: '<div>マイホームです。</div>'
//      },
//      //beforeEnter: function (to, from, next) {
//      //  // 認証されていない状態でアクセスした時はloginページに遷移する
//      //  if (!Auth.loggedIn()) {
//      //    next({
//      //      path: '/login',
//      //      query: { redirect: to.fullPath }
//      //    })
//      //  } else {
//      //    // 認証済みであればそのままユーザー詳細ページへ進む
//      //    next()
//      //  }
//      //}
//    },
//    //{
//    //  path: '/login',
//    //  component: Login
//    //},
//    //{
//    //  path: '/logout',
//    //  beforeEnter: function (to, from, next) {
//    //    Auth.logout()
//    //    next('/')
//    //  }
//    //},
//    {
//      path: uriPrefix + '/',
//      component: MemberList
//    },
//    {
//      path: uriPrefix + '/:memberId/profile',
//      component: MemberProfile,
//      beforeEnter: (to, from, next) => {
//        if (Number.isInteger(parseInt(to.params.memberId)) !== true) {
//          next('/members')
//        } else {
//          next()
//        }
//      }
//    },
//    {
//      path: uriPrefix + '/:memberId/posts',
//      component: MemberPosts,
//      beforeEnter: (to, from, next) => {
//        if (Number.isInteger(parseInt(to.params.memberId)) !== true) {
//          next('/members')
//        } else {
//          next()
//        }
//      }
//    },
//    //{
//    //  path: '/member/:memberId',
//    //  component: MemberProfile
//    //  children: [
//    //    {
//    //      // /member/:memberId/profile がマッチした時に
//    //      // MemberProfileコンポーネントはMemberコンポーネントの <router-view> 内部でレンダリングされます
//    //      path: 'profile',
//    //      component: MemberProfile
//    //    },
//    //    {
//    //      // /member/:memberId/posts がマッチした時に
//    //      // MemberPostsコンポーネントはMemberコンポーネントの <router-view> 内部でレンダリングされます
//    //      path: 'posts',
//    //      component: MemberPosts
//    //    }
//    //  ]
//    //},
//    // 現在のURLが定義したルートのいずれにもマッチしなかった時に/notfoundに遷移する
    { path: uriPrefix + '/notfound', component: NotFound },
    { path: uriPrefix + '*', redirect: '/notfound' }
  ]
})

//router.beforeEach((to, from, next) => {
//  //var $headerNav = $('#header-nav');
//  //if ($headerNav.hasClass('show')) $headerNav.collapse('hide');
//  //next();
//  //// ユーザー一覧ページへアクセスした時に/topへリダイレクトする例
//  //if (to.path === '/members') {
//  //  next('/top')
//  //} else {
//  //  // 引数なしでnextを呼び出すと通常通りの遷移が行われる
//  //  next()
//  //}
//})

//// Dummy Auth
//var Auth = {
//  login: function (email, pass, cb) {
//    // ダミーデータを使った擬似ログイン
//    setTimeout(function () {
//      if (email === 'sample@example.com' && pass === 'password') {
//        // ログイン成功時はローカルストレージにtokenを保存する
//        localStorage.token = Math.random().toString(36).substring(7)
//        if (cb) { cb(true) }
//      } else {
//        if (cb) { cb(false) }
//      }
//    }, 0)
//  },
//
//  logout: function () {
//    delete localStorage.token
//  },
//
//  loggedIn: function () {
//    // ローカルストレージにtokenがあればログイン状態とみなす
//    return !!localStorage.token
//  }
//}
//
//var Login = {
//  template: '#login',
//  data: function () {
//    return {
//      email: 'sample@example.com',
//      pass: '',
//      error: false
//    }
//  },
//  methods: {
//    login: function () {
//      Auth.login(this.email, this.pass, (function (loggedIn) {
//        if (!loggedIn) {
//          this.error = true
//        } else {
//          // redirectパラメーターが付いている場合はそのパスに遷移
//          this.$router.replace(this.$route.query.redirect || '/')
//        }
//      }).bind(this))
//    }
//  }
//}

// ルーターのインスタンスをrootとなるVueインスタンスに渡します
var app = new Vue({
  router: router,
  i18n: i18n,
  methods: {
    //hideNaveMenu2: function () {
    //  $('#header-nav').collapse('hide')
    //}
  }
}).$mount('#app')



/***/ }),

/***/ "./src/js/translations/ja-message.json":
/*!*********************************************!*\
  !*** ./src/js/translations/ja-message.json ***!
  \*********************************************/
/*! exports provided: message, default */
/***/ (function(module) {

module.exports = {"message":{"An unexpected error has occurred":"意図しないエラーが発生しました","Back":"戻る","Check your email for the instructions to reset your password":"メールに記載されているURLにアクセスし、パスワードを再設定してください。","Congratulations, you are now a registered user!":"メンバー登録が完了しました。","Edit Profile":"プロフィール編集","Edit your profile":"プロフィールを編集する","Email":"メールアドレス","File Not Found":"見つかりません","Forgot Your Password?":"パスワードを忘れた場合はこちら","Hi, %(name)s!":"こんにちは, %(name)s!","Invalid name or password":"ユーザ名かパスワードが正しくありません。","Last Login":"最終ログイン日","Last seen on":"最終アクセス日時","Login":"ログイン","Logout":"ログアウト","Name":"ユーザ名","New User?":"新規メンバー登録","Password":"パスワード","Please log in to access this page.":"ログインが必要です。","Please use a different email address.":"そのメールアドレスは登録できません。","Please use a different name.":"そのユーザ名は登録できません。","Register":"登録する","Registered at":"登録日時","Remember Me":"次回から自動的にログイン","Repeat Password":"確認用パスワード","Request Password Reset":"送信する","Reset Password":"パスワード再設定手続き","Reset Your Password":"新しいパスワードを設定する","Self-introduction":"自己紹介","Sign In":"ログイン","Submit":"送信する","The administrator has been notified. Sorry for the inconvenience!":"ご不便をおかけして申し訳ございません。サイト管理者に通知しました。","Top":"トップ","Username":"ユーザ","Your changes have been saved.":"変更しました。","Your password has been reset.":"パスワード再設定が完了しました。"}};

/***/ })

/******/ });
//# sourceMappingURL=members.js.map