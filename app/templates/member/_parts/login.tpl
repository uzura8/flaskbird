<form action="[[ url_for('member.login') ]]" method="post">
[[ form.hidden_tag() ]]

<div class="field">
	<label class="label">[[ form.name.label ]]</label>
	<div class="control">
		[[ form.name(size=32, class_='input') ]]
	</div>
	[% if form.name.errors %]
	<ul class="help is-danger">
	[% for error in form.name.errors %]
		<li>[[ error ]]</li>
	[% endfor %]
	<ul>
	[% endif %]
</div>

<div class="field">
	<label class="label">[[ form.password.label ]]</label>
	<div class="control">
		[[ form.password(size=32, class_='input') ]]
	</div>
	[% if form.password.errors %]
	<ul class="help is-danger">
	[% for error in form.password.errors %]
		<li>[[ error ]]</li>
	[% endfor %]
	<ul>
	[% endif %]
</div>

<div class="field">
  <div class="control">
    [[ form.remember_me(class_='checkbox') ]] [[ form.remember_me.label ]]
  </div>
</div>

<div class="field">
  <div class="control">[[ form.submit(class_='button is-primary') ]]</div>
</div>

<ul class="field">
  <li><a href="[[ url_for('member.reset_password_request') ]]">[[ _('Forgot Your Password?') ]]</a></li>
  <li><a href="[[ url_for('member.register') ]]">[[ _('New User?') ]]</a></li>
</ul>

</form>
