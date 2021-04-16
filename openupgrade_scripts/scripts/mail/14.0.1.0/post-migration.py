from openupgradelib import openupgrade

def fill_mail_tracking_value_field(env):
    openupgrade.logged_query(
        env.cr, """
        UPDATE mail_tracking_value mtv
        SET field = imf.id
        FROM ir_model_fields imf
        WHERE imf.name = mtv.{}
        AND imf.model = 'mail.tracking.value'
        """.format(openupgrade.get_legacy_name("field"))
    )

@openupgrade.migrate()
def migrate(env, version):
    fill_mail_tracking_value_field(env)
    openupgrade.load_data(
        env.cr, "mail", "openupgrade_scripts/scripts/mail/14.0.1.0/noupdate_changes.xml")
    openupgrade.delete_records_safely_by_xml_id(
        env, [
            "mail.mail_followers_read_write_own",
        ]
    )