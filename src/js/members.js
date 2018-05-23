'use strict';

const common = require('./common.js');
const locale = common.locale;
const translations = common.translations;
const moment = common.moment;
const axios = common.axios;

var Vue = require('vue');

var Buefy = require('buefy');
Vue.use(Buefy.default);
//import 'buefy/lib/buefy.css'
//Vue.component(Buefy.default.Loading.name, Buefy.default.Loading);

import VueI18n from 'vue-i18n';
Vue.use(VueI18n);
var i18n = new VueI18n({
  locale: locale,
  fallbackLocale: 'en',
  messages: translations
});

Vue.filter('moment', function (date) {
  return moment(date).format('LLL');
});

var VueRouter = require('vue-router');
Vue.use(VueRouter);


var uriPrefix = '/members';
var MemberList = {
  // HTML上のscriptタグのidを指定する
  template: '#member-list',
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
  template:
    '<div class="member-profile">' + 
      '<h3>こちらはユーザー {{ $route.params.memberId }} のプロフィールページです。</h3>' +
    '</div>'
}

// ユーザー詳細ページ内で部分的に表示されるユーザーの投稿ページ
var MemberPosts = {
  template:
    '<div class="member-posts">' + 
      '<h3>こちらはユーザー {{ $route.params.memberId }} の投稿ページです。</h3>' +
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
}).$mount('#container')

