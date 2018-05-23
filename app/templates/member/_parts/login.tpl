<form action="[[ url_for('member.login') ]]" method="post">
[[ g.login_form.hidden_tag() ]]

<div class="field">
  [[ g.login_form.name.label(class_='label') ]]
  <div class="control">
    [[ g.login_form.name(size=32, class_='input') ]]
  </div>
  [% if g.login_form.name.errors %]
  <ul class="help is-danger">
  [% for error in g.login_form.name.errors %]
    <li>[[ error ]]</li>
  [% endfor %]
  <ul>
  [% endif %]
</div>

<div class="field">
  [[ g.login_form.password.label(class_='label') ]]
  <div class="control">
    [[ g.login_form.password(size=32, class_='input') ]]
  </div>
  [% if g.login_form.password.errors %]
  <ul class="help is-danger">
  [% for error in g.login_form.password.errors %]
    <li>[[ error ]]</li>
  [% endfor %]
  <ul>
  [% endif %]
</div>

<div class="field">
  <div class="control">
    [[ g.login_form.remember_me(class_='checkbox', id='nav_remember_me') ]]
    [[ g.login_form.remember_me.label(for='nav_remember_me') ]]
  </div>
</div>

<div class="field">
  <div class="control">[[ g.login_form.submit(class_='button is-primary') ]]</div>
</div>

<ul class="field">
  <li><a href="[[ url_for('member.reset_password_request') ]]">[[ _('Forgot Your Password?') ]]</a></li>
  <li><a href="[[ url_for('member.register') ]]">[[ _('New User?') ]]</a></li>
</ul>

</form>
