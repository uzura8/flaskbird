[% if current_user.is_authenticated %]
        <b-dropdown position="is-bottom-left" v-cloak>
          <button class="button is-primary" slot="trigger">
            <i class="icon is-24x24">
              <img src="[[ url_media(current_user.file_name, '200x200xc') ]]" alt="[[ current_user.name ]]">
            </i>
            <span class="is-hidden-touch">[[ current_user.name ]]</span>
            <i class="icon fas fa-caret-down"></i>
          </button>

          <b-dropdown-item value="home" has-link>
            <a href="[[ url_for('member.index') ]]">
              <i class="icon fas fa-home"></i>
              [[ _('Home') ]]
            </a>
          </b-dropdown-item>
          <b-dropdown-item value="settings">
            <i class="icon fas fa-cog"></i>
            Settings
          </b-dropdown-item>
          <b-dropdown-item value="logout" has-link>
            <a href="[[ url_for('member.logout') ]]">
              <i class="icon fas fa-sign-out-alt"></i>
              [[ _('Logout') ]]
            </a>
          </b-dropdown-item>
        </b-dropdown>
[% else %]
        <b-dropdown position="is-bottom-left">
          <button class="button is-primary" slot="trigger">
            <i class="icon fas fa-user"></i>
            <span>Login</span>
            <i class="icon fas fa-caret-down"></i>
          </button>
          <b-dropdown-item custom paddingless v-cloak>
            <div class="modal-card is-marginless">
              <section class="modal-card-body">
              [% include "member/_parts/login.tpl" %]
              </section>
            </div>
          </b-dropdown-item>
        </b-dropdown>
[% endif %]
