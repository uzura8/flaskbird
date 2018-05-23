<form action="[[ url_for('member.login') ]]" method="post">
[[ g.login_form.hidden_tag() ]]

<div class="field">
	<label class="label">[[ g.login_form.name.label ]]</label>
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
	<label class="label">[[ g.login_form.password.label ]]</label>
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
    [[ g.login_form.remember_me(class_='checkbox') ]] [[ g.login_form.remember_me.label ]]
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
