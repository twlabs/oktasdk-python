from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.app.AppInstance import AppInstance
from okta.models.role.Role import Role
from okta.models.usergroup import UserGroup


class AdminRolesClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/users'
        ApiClient.__init__(self, *args, **kwargs)

    def get_user_admin_roles(self, uid):
        """Get all roles assigned to a user.

        :param uid: the user id
        :type uid: str
        :rtype: list of Role
        """
        response = ApiClient.get_path(self, '/{0}/roles'.format(uid))
        return Utils.deserialize(response.text, Role)

    def assign_roles_to_user(self, uid, role_type):
        """Assigns a role to a user.

        :param uid: User id: str
        :param role_type: Role type: str
        :return: Role
        """
        data = {
            'type': role_type
        }
        response = ApiClient.post_path(self, '/{0}/roles'.format(uid), data)
        return Utils.deserialize(response.text, Role)

    def unassign_role_from_user(self, uid, rid):
        """Unassigns a role from a user.

        :param uid: User id: str
        :param rid: Role id: str
        :return: None
        """
        ApiClient.delete_path(
            self,
            '/{uid}/roles/{rid}'.format(uid=uid, rid=rid)
        )

    def get_group_targets_for_user_role_assignment(self, uid, rid):
        """Lists all group targets for a USER_ADMIN role assignment.

        :param uid: User id: str
        :param rid: Role id: str
        :return: list of Groups
        """
        response = ApiClient.get_path(
            self,
            '/{uid}/roles/{rid}/targets/groups'.format(uid=uid, rid=rid)
        )
        return Utils.deserialize(response.text, UserGroup)

    def add_group_target_for_user_admin_role(self, uid, rid, gid):
        """Adds a group target for a USER_ADMIN role assignment.

        :param uid: User id: str
        :param rid: Role id: str
        :param gid: Group id: str
        :return: None
        """
        ApiClient.put_path(
            self,
            '/{uid}/roles/{rid}/targets/groups/{gid}'.format(
                uid=uid,
                rid=rid,
                gid=gid
            )
        )

    def remove_group_target_from_user_admin_role(self, uid, rid, gid):
        """Removes a group target from a USER_ADMIN role assignment.

        :param uid: User id: str
        :param rid: Role id: str
        :param gid: Group id: str
        :return: None
        """
        ApiClient.delete_path(
            self,
            '/{uid}/roles/{rid}/targets/groups/{gid}'.format(
                uid=uid,
                rid=rid,
                gid=gid
            )
        )

    def get_app_targets_for_app_role(self, uid, rid):
        """Lists all app targets for an APP_ADMIN role assignment.

                :param uid: User id: str
                :param rid: Role id: str
                :return: list of Catalog Apps
                """
        response = ApiClient.get_path(
            self,
            '/{uid}/roles/{rid}/targets/catalog/apps'.format(uid=uid, rid=rid)
        )
        return Utils.deserialize(response.text, AppInstance)

    def add_app_target_to_app_admin_role(self, uid, rid, app_name):
        """Adds a app target to an APP_ADMIN role assignment.

        :param uid: User id: str
        :param rid: Role id: str
        :param app_name: App name: str
        :return: None
        """
        return ApiClient.put_path(
            self,
            '/{uid}/roles/{rid}/targets/catalog/apps/{app_name}'.format(
                uid=uid,
                rid=rid,
                app_name=app_name
            )
        )

    def add_app_instance_target_to_app_admin_role(self, uid, rid, app_name,
                                                  app_instance_id):
        """Assing the role APP_ADMIN to a app target instance 

        :param uid: User id: str
        :param rid: Role id: str
        :param app_name: App name: str
        :param app_instance_id: Instance id: str  
        :return: None
        """
        return ApiClient.put_path(
            self,
            f'/{uid}/roles/{rid}/targets/catalog/apps/{app_name}/'
            f'{app_instance_id}'
        )

    def remove_app_target_to_app_admin_role(self, uid, rid, app_name):
        """Removes a app target to an APP_ADMIN role assignment.

        :param uid: User id: str
        :param rid: Role id: str
        :param app_name: App name: str
        :return: None
        """
        ApiClient.delete_path(
            self,
            '/{uid}/roles/{rid}/targets/catalog/apps/{app_name}'.format(
                uid=uid,
                rid=rid,
                app_name=app_name
            )
        )
