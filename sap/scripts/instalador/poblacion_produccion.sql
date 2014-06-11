--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.usuarios_usuarios DROP CONSTRAINT usuarios_usuarios_user_id_fkey;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT user_id_refs_id_c0d12874;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT user_id_refs_id_4dc23c39;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT user_id_refs_id_40c41112;
ALTER TABLE ONLY public."tipoitem_tipoitem_listaAtributo" DROP CONSTRAINT "tipoitem_tipoitem_listaAtributo_listaatributo_id_fkey";
ALTER TABLE ONLY public."tipoitem_tipoitem_listaAtributo" DROP CONSTRAINT tipoitem_id_refs_id_e4d37b53;
ALTER TABLE ONLY public.tipoatributo_tipoatributo_proyecto DROP CONSTRAINT tipoatributo_tipoatributo_proyecto_proyectos_id_fkey;
ALTER TABLE ONLY public.tipoatributo_tipoatributo_proyecto DROP CONSTRAINT tipoatributo_id_refs_id_58907e1e;
ALTER TABLE ONLY public.solicitudes_votos DROP CONSTRAINT solicitudes_votos_solicitud_id_fkey;
ALTER TABLE ONLY public.solicitudes_votos DROP CONSTRAINT solicitudes_votos_miembro_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_usuario_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_proyecto_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_item_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_fase_id_fkey;
ALTER TABLE ONLY public.solicitudes_credenciales DROP CONSTRAINT solicitudes_credenciales_usuario_id_fkey;
ALTER TABLE ONLY public.solicitudes_credenciales DROP CONSTRAINT solicitudes_credenciales_proyecto_id_fkey;
ALTER TABLE ONLY public.solicitudes_credenciales DROP CONSTRAINT solicitudes_credenciales_item_id_fkey;
ALTER TABLE ONLY public.solicitudes_credenciales DROP CONSTRAINT solicitudes_credenciales_fase_id_fkey;
ALTER TABLE ONLY public.roles_roles DROP CONSTRAINT roles_roles_group_ptr_id_fkey;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT roles_id_refs_group_ptr_id_11e17ff0;
ALTER TABLE ONLY public.relaciones_relaciones DROP CONSTRAINT relaciones_relaciones_padre_id_fkey;
ALTER TABLE ONLY public.proyectos_proyectos DROP CONSTRAINT proyectos_proyectos_lider_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase DROP CONSTRAINT lineabase_lineabase_proyecto_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase_items DROP CONSTRAINT lineabase_lineabase_items_items_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase DROP CONSTRAINT lineabase_lineabase_fase_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase_items DROP CONSTRAINT lineabase_id_refs_id_398bc2f5;
ALTER TABLE ONLY public.items_valoritem DROP CONSTRAINT items_valoritem_proyecto_id_fkey;
ALTER TABLE ONLY public.items_valoritem DROP CONSTRAINT items_valoritem_item_id_fkey;
ALTER TABLE ONLY public.items_valoritem DROP CONSTRAINT items_valoritem_fase_id_fkey;
ALTER TABLE ONLY public.items_items DROP CONSTRAINT items_items_tipo_item_id_fkey;
ALTER TABLE ONLY public.items_items DROP CONSTRAINT items_items_proyecto_id_fkey;
ALTER TABLE ONLY public.items_items DROP CONSTRAINT items_items_fase_id_fkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT group_id_refs_id_f4b32aac;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT fases_id_refs_id_f013efc7;
ALTER TABLE ONLY public.fases_fases DROP CONSTRAINT fases_fases_proyecto_id_fkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT content_type_id_refs_id_d043b34a;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT content_type_id_refs_id_93d2d1f8;
ALTER TABLE ONLY public.comite_comite_miembros DROP CONSTRAINT comite_id_refs_id_b93ed40d;
ALTER TABLE ONLY public.comite_comite DROP CONSTRAINT comite_comite_proyecto_id_fkey;
ALTER TABLE ONLY public.comite_comite_miembros DROP CONSTRAINT comite_comite_miembros_usuarios_id_fkey;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_permission_id_fkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fkey;
DROP INDEX public."tipoitem_tipoitem_listaAtributo_tipoitem_id";
DROP INDEX public."tipoitem_tipoitem_listaAtributo_listaatributo_id";
DROP INDEX public.tipoatributo_tipoatributo_proyecto_tipoatributo_id;
DROP INDEX public.tipoatributo_tipoatributo_proyecto_proyectos_id;
DROP INDEX public.tipoatributo_tipoatributo_nombre_like;
DROP INDEX public.solicitudes_votos_solicitud_id;
DROP INDEX public.solicitudes_votos_miembro_id;
DROP INDEX public.solicitudes_solicitudes_usuario_id;
DROP INDEX public.solicitudes_solicitudes_proyecto_id;
DROP INDEX public.solicitudes_solicitudes_item_id;
DROP INDEX public.solicitudes_solicitudes_fase_id;
DROP INDEX public.solicitudes_credenciales_usuario_id;
DROP INDEX public.solicitudes_credenciales_proyecto_id;
DROP INDEX public.solicitudes_credenciales_item_id;
DROP INDEX public.solicitudes_credenciales_fase_id;
DROP INDEX public.roles_roles_fases_roles_id;
DROP INDEX public.roles_roles_fases_fases_id;
DROP INDEX public.relaciones_relaciones_padre_id;
DROP INDEX public.proyectos_proyectos_lider_id;
DROP INDEX public.lineabase_lineabase_proyecto_id;
DROP INDEX public.lineabase_lineabase_items_lineabase_id;
DROP INDEX public.lineabase_lineabase_items_items_id;
DROP INDEX public.lineabase_lineabase_fase_id;
DROP INDEX public.items_valoritem_proyecto_id;
DROP INDEX public.items_valoritem_item_id;
DROP INDEX public.items_valoritem_fase_id;
DROP INDEX public.items_items_tipo_item_id;
DROP INDEX public.items_items_proyecto_id;
DROP INDEX public.items_items_fase_id;
DROP INDEX public.fases_fases_proyecto_id;
DROP INDEX public.django_session_session_key_like;
DROP INDEX public.django_session_expire_date;
DROP INDEX public.django_cron_cronjoblog_start_time;
DROP INDEX public.django_cron_cronjoblog_ran_at_time;
DROP INDEX public.django_cron_cronjoblog_end_time;
DROP INDEX public.django_cron_cronjoblog_code_like;
DROP INDEX public.django_cron_cronjoblog_code;
DROP INDEX public.django_cron_cronjoblog_63e2740d;
DROP INDEX public.django_cron_cronjoblog_495fb183;
DROP INDEX public.django_cron_cronjoblog_1fe0e40b;
DROP INDEX public.django_admin_log_user_id;
DROP INDEX public.django_admin_log_content_type_id;
DROP INDEX public.comite_comite_proyecto_id;
DROP INDEX public.comite_comite_miembros_usuarios_id;
DROP INDEX public.comite_comite_miembros_comite_id;
DROP INDEX public.auth_user_username_like;
DROP INDEX public.auth_user_user_permissions_user_id;
DROP INDEX public.auth_user_user_permissions_permission_id;
DROP INDEX public.auth_user_groups_user_id;
DROP INDEX public.auth_user_groups_group_id;
DROP INDEX public.auth_permission_content_type_id;
DROP INDEX public.auth_group_permissions_permission_id;
DROP INDEX public.auth_group_permissions_group_id;
DROP INDEX public.auth_group_name_like;
ALTER TABLE ONLY public.usuarios_usuarios DROP CONSTRAINT usuarios_usuarios_pkey;
ALTER TABLE ONLY public.tipoitem_tipoitem DROP CONSTRAINT tipoitem_tipoitem_pkey;
ALTER TABLE ONLY public."tipoitem_tipoitem_listaAtributo" DROP CONSTRAINT "tipoitem_tipoitem_listaAtributo_pkey";
ALTER TABLE ONLY public."tipoitem_tipoitem_listaAtributo" DROP CONSTRAINT "tipoitem_tipoitem_listaAtribut_tipoitem_id_listaatributo_id_key";
ALTER TABLE ONLY public.tipoitem_listaatributo DROP CONSTRAINT tipoitem_listaatributo_pkey;
ALTER TABLE ONLY public.tipoatributo_tipoatributo_proyecto DROP CONSTRAINT tipoatributo_tipoatributo_proyecto_pkey;
ALTER TABLE ONLY public.tipoatributo_tipoatributo_proyecto DROP CONSTRAINT tipoatributo_tipoatributo_proy_tipoatributo_id_proyectos_id_key;
ALTER TABLE ONLY public.tipoatributo_tipoatributo DROP CONSTRAINT tipoatributo_tipoatributo_pkey;
ALTER TABLE ONLY public.tipoatributo_tipoatributo DROP CONSTRAINT tipoatributo_tipoatributo_nombre_key;
ALTER TABLE ONLY public.tipoatributo_texto DROP CONSTRAINT tipoatributo_texto_pkey;
ALTER TABLE ONLY public.tipoatributo_numerico DROP CONSTRAINT tipoatributo_numerico_pkey;
ALTER TABLE ONLY public.tipoatributo_logico DROP CONSTRAINT tipoatributo_logico_pkey;
ALTER TABLE ONLY public.tipoatributo_imagen DROP CONSTRAINT tipoatributo_imagen_pkey;
ALTER TABLE ONLY public.tipoatributo_fecha DROP CONSTRAINT tipoatributo_fecha_pkey;
ALTER TABLE ONLY public.tipoatributo_archivoexterno DROP CONSTRAINT tipoatributo_archivoexterno_pkey;
ALTER TABLE ONLY public.solicitudes_votos DROP CONSTRAINT solicitudes_votos_pkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_pkey;
ALTER TABLE ONLY public.solicitudes_credenciales DROP CONSTRAINT solicitudes_credenciales_pkey;
ALTER TABLE ONLY public.roles_roles DROP CONSTRAINT roles_roles_pkey;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT roles_roles_fases_roles_id_fases_id_key;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT roles_roles_fases_pkey;
ALTER TABLE ONLY public.relaciones_relaciones DROP CONSTRAINT relaciones_relaciones_pkey;
ALTER TABLE ONLY public.proyectos_proyectos DROP CONSTRAINT proyectos_proyectos_pkey;
ALTER TABLE ONLY public.lineabase_lineabase DROP CONSTRAINT lineabase_lineabase_pkey;
ALTER TABLE ONLY public.lineabase_lineabase_items DROP CONSTRAINT lineabase_lineabase_items_pkey;
ALTER TABLE ONLY public.lineabase_lineabase_items DROP CONSTRAINT lineabase_lineabase_items_lineabase_id_items_id_key;
ALTER TABLE ONLY public.items_valoritem DROP CONSTRAINT items_valoritem_pkey;
ALTER TABLE ONLY public.items_listavalores DROP CONSTRAINT items_listavalores_pkey;
ALTER TABLE ONLY public.items_items DROP CONSTRAINT items_items_pkey;
ALTER TABLE ONLY public.fases_fases DROP CONSTRAINT fases_fases_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_cron_cronjoblog DROP CONSTRAINT django_cron_cronjoblog_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_key;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.comite_comite DROP CONSTRAINT comite_comite_pkey;
ALTER TABLE ONLY public.comite_comite_miembros DROP CONSTRAINT comite_comite_miembros_pkey;
ALTER TABLE ONLY public.comite_comite_miembros DROP CONSTRAINT comite_comite_miembros_comite_id_usuarios_id_key;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
ALTER TABLE public."tipoitem_tipoitem_listaAtributo" ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoitem_tipoitem ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoitem_listaatributo ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_tipoatributo_proyecto ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_tipoatributo ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_texto ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_numerico ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_logico ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_imagen ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_fecha ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tipoatributo_archivoexterno ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.solicitudes_votos ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.solicitudes_solicitudes ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.solicitudes_credenciales ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.roles_roles_fases ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.relaciones_relaciones ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.proyectos_proyectos ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.lineabase_lineabase_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.lineabase_lineabase ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_valoritem ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_listavalores ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.fases_fases ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_cron_cronjoblog ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.comite_comite_miembros ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.comite_comite ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
DROP TABLE public.usuarios_usuarios;
DROP SEQUENCE public."tipoitem_tipoitem_listaAtributo_id_seq";
DROP TABLE public."tipoitem_tipoitem_listaAtributo";
DROP SEQUENCE public.tipoitem_tipoitem_id_seq;
DROP TABLE public.tipoitem_tipoitem;
DROP SEQUENCE public.tipoitem_listaatributo_id_seq;
DROP TABLE public.tipoitem_listaatributo;
DROP SEQUENCE public.tipoatributo_tipoatributo_proyecto_id_seq;
DROP TABLE public.tipoatributo_tipoatributo_proyecto;
DROP SEQUENCE public.tipoatributo_tipoatributo_id_seq;
DROP TABLE public.tipoatributo_tipoatributo;
DROP SEQUENCE public.tipoatributo_texto_id_seq;
DROP TABLE public.tipoatributo_texto;
DROP SEQUENCE public.tipoatributo_numerico_id_seq;
DROP TABLE public.tipoatributo_numerico;
DROP SEQUENCE public.tipoatributo_logico_id_seq;
DROP TABLE public.tipoatributo_logico;
DROP SEQUENCE public.tipoatributo_imagen_id_seq;
DROP TABLE public.tipoatributo_imagen;
DROP SEQUENCE public.tipoatributo_fecha_id_seq;
DROP TABLE public.tipoatributo_fecha;
DROP SEQUENCE public.tipoatributo_archivoexterno_id_seq;
DROP TABLE public.tipoatributo_archivoexterno;
DROP SEQUENCE public.solicitudes_votos_id_seq;
DROP TABLE public.solicitudes_votos;
DROP SEQUENCE public.solicitudes_solicitudes_id_seq;
DROP TABLE public.solicitudes_solicitudes;
DROP SEQUENCE public.solicitudes_credenciales_id_seq;
DROP TABLE public.solicitudes_credenciales;
DROP SEQUENCE public.roles_roles_fases_id_seq;
DROP TABLE public.roles_roles_fases;
DROP TABLE public.roles_roles;
DROP SEQUENCE public.relaciones_relaciones_id_seq;
DROP TABLE public.relaciones_relaciones;
DROP SEQUENCE public.proyectos_proyectos_id_seq;
DROP TABLE public.proyectos_proyectos;
DROP SEQUENCE public.lineabase_lineabase_items_id_seq;
DROP TABLE public.lineabase_lineabase_items;
DROP SEQUENCE public.lineabase_lineabase_id_seq;
DROP TABLE public.lineabase_lineabase;
DROP SEQUENCE public.items_valoritem_id_seq;
DROP TABLE public.items_valoritem;
DROP SEQUENCE public.items_listavalores_id_seq;
DROP TABLE public.items_listavalores;
DROP SEQUENCE public.items_items_id_seq;
DROP TABLE public.items_items;
DROP SEQUENCE public.fases_fases_id_seq;
DROP TABLE public.fases_fases;
DROP TABLE public.django_session;
DROP SEQUENCE public.django_cron_cronjoblog_id_seq;
DROP TABLE public.django_cron_cronjoblog;
DROP SEQUENCE public.django_content_type_id_seq;
DROP TABLE public.django_content_type;
DROP SEQUENCE public.django_admin_log_id_seq;
DROP TABLE public.django_admin_log;
DROP SEQUENCE public.comite_comite_miembros_id_seq;
DROP TABLE public.comite_comite_miembros;
DROP SEQUENCE public.comite_comite_id_seq;
DROP TABLE public.comite_comite;
DROP SEQUENCE public.auth_user_user_permissions_id_seq;
DROP TABLE public.auth_user_user_permissions;
DROP SEQUENCE public.auth_user_id_seq;
DROP SEQUENCE public.auth_user_groups_id_seq;
DROP TABLE public.auth_user_groups;
DROP TABLE public.auth_user;
DROP SEQUENCE public.auth_permission_id_seq;
DROP TABLE public.auth_permission;
DROP SEQUENCE public.auth_group_permissions_id_seq;
DROP TABLE public.auth_group_permissions;
DROP SEQUENCE public.auth_group_id_seq;
DROP TABLE public.auth_group;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO sap;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO sap;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO sap;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO sap;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO sap;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO sap;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO sap;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO sap;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO sap;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO sap;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO sap;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO sap;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: comite_comite; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE comite_comite (
    id integer NOT NULL,
    nombre character varying(30),
    proyecto_id integer NOT NULL
);


ALTER TABLE public.comite_comite OWNER TO sap;

--
-- Name: comite_comite_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE comite_comite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comite_comite_id_seq OWNER TO sap;

--
-- Name: comite_comite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE comite_comite_id_seq OWNED BY comite_comite.id;


--
-- Name: comite_comite_miembros; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE comite_comite_miembros (
    id integer NOT NULL,
    comite_id integer NOT NULL,
    usuarios_id integer NOT NULL
);


ALTER TABLE public.comite_comite_miembros OWNER TO sap;

--
-- Name: comite_comite_miembros_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE comite_comite_miembros_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comite_comite_miembros_id_seq OWNER TO sap;

--
-- Name: comite_comite_miembros_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE comite_comite_miembros_id_seq OWNED BY comite_comite_miembros.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO sap;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO sap;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO sap;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO sap;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_cron_cronjoblog; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE django_cron_cronjoblog (
    id integer NOT NULL,
    code character varying(64) NOT NULL,
    start_time timestamp with time zone NOT NULL,
    end_time timestamp with time zone NOT NULL,
    is_success boolean NOT NULL,
    message text NOT NULL,
    ran_at_time time without time zone
);


ALTER TABLE public.django_cron_cronjoblog OWNER TO sap;

--
-- Name: django_cron_cronjoblog_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE django_cron_cronjoblog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_cron_cronjoblog_id_seq OWNER TO sap;

--
-- Name: django_cron_cronjoblog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE django_cron_cronjoblog_id_seq OWNED BY django_cron_cronjoblog.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO sap;

--
-- Name: fases_fases; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE fases_fases (
    id integer NOT NULL,
    nombre character varying(20),
    nombre_eliminado character varying(20),
    descripcion character varying(300),
    estado character varying(2),
    fechainicio date,
    duracion integer,
    proyecto_id integer NOT NULL,
    is_active boolean NOT NULL,
    orden integer
);


ALTER TABLE public.fases_fases OWNER TO sap;

--
-- Name: fases_fases_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE fases_fases_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fases_fases_id_seq OWNER TO sap;

--
-- Name: fases_fases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE fases_fases_id_seq OWNED BY fases_fases.id;


--
-- Name: items_items; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE items_items (
    id integer NOT NULL,
    nombre character varying(30),
    version integer,
    prioridad integer,
    estado character varying(20),
    descripcion character varying(300),
    observaciones character varying(300),
    "costoMonetario" integer,
    "costoTemporal" integer,
    complejidad integer,
    fase_id integer NOT NULL,
    proyecto_id integer NOT NULL,
    is_active boolean NOT NULL,
    tipo_item_id integer NOT NULL,
    padre integer,
    lb integer
);


ALTER TABLE public.items_items OWNER TO sap;

--
-- Name: items_items_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE items_items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_items_id_seq OWNER TO sap;

--
-- Name: items_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE items_items_id_seq OWNED BY items_items.id;


--
-- Name: items_listavalores; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE items_listavalores (
    id integer NOT NULL,
    nombre character varying(20),
    nombre_atributo character varying(20),
    tipo_dato character varying(20),
    valor_texto character varying(300),
    valor_numerico integer,
    valor_fecha character varying(15),
    valor_archivoexterno character varying(100),
    valor_imagen character varying(100),
    orden integer
);


ALTER TABLE public.items_listavalores OWNER TO sap;

--
-- Name: items_listavalores_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE items_listavalores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_listavalores_id_seq OWNER TO sap;

--
-- Name: items_listavalores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE items_listavalores_id_seq OWNED BY items_listavalores.id;


--
-- Name: items_valoritem; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE items_valoritem (
    id integer NOT NULL,
    nombre character varying(30),
    item_id integer NOT NULL,
    valor_id integer,
    tabla_valor_nombre character varying(40),
    nombre_atributo character varying(40),
    tipo_dato character varying(40),
    version integer,
    orden integer,
    fase_id integer NOT NULL,
    proyecto_id integer NOT NULL
);


ALTER TABLE public.items_valoritem OWNER TO sap;

--
-- Name: items_valoritem_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE items_valoritem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_valoritem_id_seq OWNER TO sap;

--
-- Name: items_valoritem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE items_valoritem_id_seq OWNED BY items_valoritem.id;


--
-- Name: lineabase_lineabase; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE lineabase_lineabase (
    id integer NOT NULL,
    numero integer NOT NULL,
    proyecto_id integer NOT NULL,
    fase_id integer NOT NULL,
    is_active boolean NOT NULL,
    descripcion character varying(300) NOT NULL,
    fecha_creacion date NOT NULL
);


ALTER TABLE public.lineabase_lineabase OWNER TO sap;

--
-- Name: lineabase_lineabase_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE lineabase_lineabase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lineabase_lineabase_id_seq OWNER TO sap;

--
-- Name: lineabase_lineabase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE lineabase_lineabase_id_seq OWNED BY lineabase_lineabase.id;


--
-- Name: lineabase_lineabase_items; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE lineabase_lineabase_items (
    id integer NOT NULL,
    lineabase_id integer NOT NULL,
    items_id integer NOT NULL
);


ALTER TABLE public.lineabase_lineabase_items OWNER TO sap;

--
-- Name: lineabase_lineabase_items_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE lineabase_lineabase_items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lineabase_lineabase_items_id_seq OWNER TO sap;

--
-- Name: lineabase_lineabase_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE lineabase_lineabase_items_id_seq OWNED BY lineabase_lineabase_items.id;


--
-- Name: proyectos_proyectos; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE proyectos_proyectos (
    id integer NOT NULL,
    nombre character varying(30) NOT NULL,
    lider_id integer,
    estado character varying(15) NOT NULL,
    fecha_inicio date NOT NULL,
    duracion integer NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.proyectos_proyectos OWNER TO sap;

--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE proyectos_proyectos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyectos_proyectos_id_seq OWNER TO sap;

--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE proyectos_proyectos_id_seq OWNED BY proyectos_proyectos.id;


--
-- Name: relaciones_relaciones; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE relaciones_relaciones (
    id integer NOT NULL,
    nombre character varying(30),
    padre_id integer NOT NULL,
    item integer,
    version integer
);


ALTER TABLE public.relaciones_relaciones OWNER TO sap;

--
-- Name: relaciones_relaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE relaciones_relaciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relaciones_relaciones_id_seq OWNER TO sap;

--
-- Name: relaciones_relaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE relaciones_relaciones_id_seq OWNED BY relaciones_relaciones.id;


--
-- Name: roles_roles; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE roles_roles (
    group_ptr_id integer NOT NULL,
    proyecto character varying(30) NOT NULL,
    descripcion text NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.roles_roles OWNER TO sap;

--
-- Name: roles_roles_fases; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE roles_roles_fases (
    id integer NOT NULL,
    roles_id integer NOT NULL,
    fases_id integer NOT NULL
);


ALTER TABLE public.roles_roles_fases OWNER TO sap;

--
-- Name: roles_roles_fases_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE roles_roles_fases_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_roles_fases_id_seq OWNER TO sap;

--
-- Name: roles_roles_fases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE roles_roles_fases_id_seq OWNED BY roles_roles_fases.id;


--
-- Name: solicitudes_credenciales; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE solicitudes_credenciales (
    id integer NOT NULL,
    nombre character varying(30),
    usuario_id integer NOT NULL,
    proyecto_id integer NOT NULL,
    fase_id integer NOT NULL,
    item_id integer NOT NULL,
    fecha_aprobacion date,
    fecha_expiracion date,
    estado character varying(50),
    observaciones character varying(500)
);


ALTER TABLE public.solicitudes_credenciales OWNER TO sap;

--
-- Name: solicitudes_credenciales_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE solicitudes_credenciales_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solicitudes_credenciales_id_seq OWNER TO sap;

--
-- Name: solicitudes_credenciales_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE solicitudes_credenciales_id_seq OWNED BY solicitudes_credenciales.id;


--
-- Name: solicitudes_solicitudes; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE solicitudes_solicitudes (
    id integer NOT NULL,
    nombre character varying(30),
    usuario_id integer NOT NULL,
    proyecto_id integer NOT NULL,
    fase_id integer NOT NULL,
    item_id integer NOT NULL,
    fecha_solicitud date,
    tiempo_solicitado integer,
    descripcion character varying(500),
    observaciones character varying(500),
    estado character varying(50),
    tiempo_esperado integer
);


ALTER TABLE public.solicitudes_solicitudes OWNER TO sap;

--
-- Name: solicitudes_solicitudes_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE solicitudes_solicitudes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solicitudes_solicitudes_id_seq OWNER TO sap;

--
-- Name: solicitudes_solicitudes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE solicitudes_solicitudes_id_seq OWNED BY solicitudes_solicitudes.id;


--
-- Name: solicitudes_votos; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE solicitudes_votos (
    id integer NOT NULL,
    miembro_id integer NOT NULL,
    solicitud_id integer NOT NULL,
    "fechaDeVotacion" date NOT NULL,
    voto character varying(2) NOT NULL
);


ALTER TABLE public.solicitudes_votos OWNER TO sap;

--
-- Name: solicitudes_votos_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE solicitudes_votos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solicitudes_votos_id_seq OWNER TO sap;

--
-- Name: solicitudes_votos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE solicitudes_votos_id_seq OWNED BY solicitudes_votos.id;


--
-- Name: tipoatributo_archivoexterno; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_archivoexterno (
    id integer NOT NULL,
    valor character varying(100) NOT NULL,
    id_item integer NOT NULL,
    nombre_atributo character varying(20) NOT NULL,
    obligatorio boolean NOT NULL
);


ALTER TABLE public.tipoatributo_archivoexterno OWNER TO sap;

--
-- Name: tipoatributo_archivoexterno_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_archivoexterno_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_archivoexterno_id_seq OWNER TO sap;

--
-- Name: tipoatributo_archivoexterno_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_archivoexterno_id_seq OWNED BY tipoatributo_archivoexterno.id;


--
-- Name: tipoatributo_fecha; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_fecha (
    id integer NOT NULL,
    valor character varying(15) NOT NULL,
    id_item integer NOT NULL,
    nombre_atributo character varying(20) NOT NULL,
    obligatorio boolean NOT NULL
);


ALTER TABLE public.tipoatributo_fecha OWNER TO sap;

--
-- Name: tipoatributo_fecha_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_fecha_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_fecha_id_seq OWNER TO sap;

--
-- Name: tipoatributo_fecha_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_fecha_id_seq OWNED BY tipoatributo_fecha.id;


--
-- Name: tipoatributo_imagen; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_imagen (
    id integer NOT NULL,
    valor character varying(100) NOT NULL,
    id_item integer NOT NULL,
    nombre_atributo character varying(20) NOT NULL,
    obligatorio boolean NOT NULL
);


ALTER TABLE public.tipoatributo_imagen OWNER TO sap;

--
-- Name: tipoatributo_imagen_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_imagen_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_imagen_id_seq OWNER TO sap;

--
-- Name: tipoatributo_imagen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_imagen_id_seq OWNED BY tipoatributo_imagen.id;


--
-- Name: tipoatributo_logico; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_logico (
    id integer NOT NULL,
    valor boolean NOT NULL,
    id_item integer NOT NULL,
    nombre_atributo character varying(20) NOT NULL,
    obligatorio boolean NOT NULL
);


ALTER TABLE public.tipoatributo_logico OWNER TO sap;

--
-- Name: tipoatributo_logico_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_logico_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_logico_id_seq OWNER TO sap;

--
-- Name: tipoatributo_logico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_logico_id_seq OWNED BY tipoatributo_logico.id;


--
-- Name: tipoatributo_numerico; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_numerico (
    id integer NOT NULL,
    valor numeric(30,10) NOT NULL,
    id_item integer NOT NULL,
    nombre_atributo character varying(20) NOT NULL,
    "precision" integer NOT NULL,
    longitud integer NOT NULL,
    obligatorio boolean NOT NULL
);


ALTER TABLE public.tipoatributo_numerico OWNER TO sap;

--
-- Name: tipoatributo_numerico_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_numerico_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_numerico_id_seq OWNER TO sap;

--
-- Name: tipoatributo_numerico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_numerico_id_seq OWNED BY tipoatributo_numerico.id;


--
-- Name: tipoatributo_texto; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_texto (
    id integer NOT NULL,
    valor character varying(300) NOT NULL,
    id_item integer NOT NULL,
    nombre_atributo character varying(20) NOT NULL,
    longitud integer NOT NULL,
    obligatorio boolean NOT NULL
);


ALTER TABLE public.tipoatributo_texto OWNER TO sap;

--
-- Name: tipoatributo_texto_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_texto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_texto_id_seq OWNER TO sap;

--
-- Name: tipoatributo_texto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_texto_id_seq OWNED BY tipoatributo_texto.id;


--
-- Name: tipoatributo_tipoatributo; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_tipoatributo (
    id integer NOT NULL,
    nombre character varying(20) NOT NULL,
    tipo character varying(16) NOT NULL,
    "precision" integer NOT NULL,
    longitud integer NOT NULL,
    obligatorio boolean NOT NULL,
    descripcion text NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.tipoatributo_tipoatributo OWNER TO sap;

--
-- Name: tipoatributo_tipoatributo_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_tipoatributo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_tipoatributo_id_seq OWNER TO sap;

--
-- Name: tipoatributo_tipoatributo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_tipoatributo_id_seq OWNED BY tipoatributo_tipoatributo.id;


--
-- Name: tipoatributo_tipoatributo_proyecto; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoatributo_tipoatributo_proyecto (
    id integer NOT NULL,
    tipoatributo_id integer NOT NULL,
    proyectos_id integer NOT NULL
);


ALTER TABLE public.tipoatributo_tipoatributo_proyecto OWNER TO sap;

--
-- Name: tipoatributo_tipoatributo_proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoatributo_tipoatributo_proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoatributo_tipoatributo_proyecto_id_seq OWNER TO sap;

--
-- Name: tipoatributo_tipoatributo_proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoatributo_tipoatributo_proyecto_id_seq OWNED BY tipoatributo_tipoatributo_proyecto.id;


--
-- Name: tipoitem_listaatributo; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoitem_listaatributo (
    id integer NOT NULL,
    id_atributo integer NOT NULL,
    id_tipoitem integer NOT NULL,
    orden integer NOT NULL,
    nombre character varying(20) NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.tipoitem_listaatributo OWNER TO sap;

--
-- Name: tipoitem_listaatributo_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoitem_listaatributo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoitem_listaatributo_id_seq OWNER TO sap;

--
-- Name: tipoitem_listaatributo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoitem_listaatributo_id_seq OWNED BY tipoitem_listaatributo.id;


--
-- Name: tipoitem_tipoitem; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE tipoitem_tipoitem (
    id integer NOT NULL,
    nombre character varying(30),
    descripcion text NOT NULL,
    id_proyecto integer NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.tipoitem_tipoitem OWNER TO sap;

--
-- Name: tipoitem_tipoitem_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE tipoitem_tipoitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoitem_tipoitem_id_seq OWNER TO sap;

--
-- Name: tipoitem_tipoitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE tipoitem_tipoitem_id_seq OWNED BY tipoitem_tipoitem.id;


--
-- Name: tipoitem_tipoitem_listaAtributo; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE "tipoitem_tipoitem_listaAtributo" (
    id integer NOT NULL,
    tipoitem_id integer NOT NULL,
    listaatributo_id integer NOT NULL
);


ALTER TABLE public."tipoitem_tipoitem_listaAtributo" OWNER TO sap;

--
-- Name: tipoitem_tipoitem_listaAtributo_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE "tipoitem_tipoitem_listaAtributo_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."tipoitem_tipoitem_listaAtributo_id_seq" OWNER TO sap;

--
-- Name: tipoitem_tipoitem_listaAtributo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE "tipoitem_tipoitem_listaAtributo_id_seq" OWNED BY "tipoitem_tipoitem_listaAtributo".id;


--
-- Name: usuarios_usuarios; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE usuarios_usuarios (
    user_id integer NOT NULL,
    telefono character varying(30) NOT NULL,
    direccion character varying(50) NOT NULL,
    especialidad character varying(50) NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public.usuarios_usuarios OWNER TO sap;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY comite_comite ALTER COLUMN id SET DEFAULT nextval('comite_comite_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY comite_comite_miembros ALTER COLUMN id SET DEFAULT nextval('comite_comite_miembros_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY django_cron_cronjoblog ALTER COLUMN id SET DEFAULT nextval('django_cron_cronjoblog_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY fases_fases ALTER COLUMN id SET DEFAULT nextval('fases_fases_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_items ALTER COLUMN id SET DEFAULT nextval('items_items_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_listavalores ALTER COLUMN id SET DEFAULT nextval('items_listavalores_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_valoritem ALTER COLUMN id SET DEFAULT nextval('items_valoritem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY lineabase_lineabase ALTER COLUMN id SET DEFAULT nextval('lineabase_lineabase_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY lineabase_lineabase_items ALTER COLUMN id SET DEFAULT nextval('lineabase_lineabase_items_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY proyectos_proyectos ALTER COLUMN id SET DEFAULT nextval('proyectos_proyectos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY relaciones_relaciones ALTER COLUMN id SET DEFAULT nextval('relaciones_relaciones_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY roles_roles_fases ALTER COLUMN id SET DEFAULT nextval('roles_roles_fases_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_credenciales ALTER COLUMN id SET DEFAULT nextval('solicitudes_credenciales_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes ALTER COLUMN id SET DEFAULT nextval('solicitudes_solicitudes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_votos ALTER COLUMN id SET DEFAULT nextval('solicitudes_votos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_archivoexterno ALTER COLUMN id SET DEFAULT nextval('tipoatributo_archivoexterno_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_fecha ALTER COLUMN id SET DEFAULT nextval('tipoatributo_fecha_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_imagen ALTER COLUMN id SET DEFAULT nextval('tipoatributo_imagen_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_logico ALTER COLUMN id SET DEFAULT nextval('tipoatributo_logico_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_numerico ALTER COLUMN id SET DEFAULT nextval('tipoatributo_numerico_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_texto ALTER COLUMN id SET DEFAULT nextval('tipoatributo_texto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_tipoatributo ALTER COLUMN id SET DEFAULT nextval('tipoatributo_tipoatributo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_tipoatributo_proyecto ALTER COLUMN id SET DEFAULT nextval('tipoatributo_tipoatributo_proyecto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoitem_listaatributo ALTER COLUMN id SET DEFAULT nextval('tipoitem_listaatributo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoitem_tipoitem ALTER COLUMN id SET DEFAULT nextval('tipoitem_tipoitem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY "tipoitem_tipoitem_listaAtributo" ALTER COLUMN id SET DEFAULT nextval('"tipoitem_tipoitem_listaAtributo_id_seq"'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_group (id, name) FROM stdin;
1	todo rol
2	desarrollador1
3	desarrollador2
4	desarrollador3
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_id_seq', 4, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	19
2	1	21
3	1	20
4	1	43
5	1	40
6	1	42
7	1	44
8	1	41
9	1	38
10	1	39
11	1	33
12	1	35
13	1	37
14	1	36
15	1	34
16	1	29
17	1	32
18	1	30
19	1	26
20	1	31
21	1	28
22	1	27
23	1	45
24	1	46
25	1	25
26	1	22
27	1	24
28	1	23
29	1	98
30	1	103
31	1	105
32	1	104
33	1	70
34	1	69
35	1	77
36	1	74
37	1	71
38	1	73
39	1	75
40	1	76
41	1	72
42	2	19
43	2	21
44	2	20
45	2	43
46	2	40
47	2	42
48	2	44
49	2	41
50	2	38
51	2	39
52	2	33
53	2	35
54	2	37
55	2	36
56	2	34
57	2	29
58	2	32
59	2	30
60	2	26
61	2	31
62	2	28
63	2	27
64	2	45
65	2	46
66	2	25
67	2	22
68	2	24
69	2	23
70	2	98
71	2	103
72	2	105
73	2	104
74	2	70
75	2	69
76	2	77
77	2	74
78	2	71
79	2	73
80	2	75
81	2	76
82	2	72
83	3	19
84	3	21
85	3	20
86	3	43
87	3	40
88	3	42
89	3	44
90	3	41
91	3	38
92	3	39
93	3	33
94	3	35
95	3	37
96	3	36
97	3	34
98	3	29
99	3	32
100	3	30
101	3	26
102	3	31
103	3	28
104	3	27
105	3	45
106	3	46
107	3	25
108	3	22
109	3	24
110	3	23
111	3	98
112	3	103
113	3	105
114	3	104
115	3	70
116	3	69
117	3	77
118	3	74
119	3	71
120	3	73
121	3	75
122	3	76
123	3	72
124	4	19
125	4	21
126	4	20
127	4	43
128	4	40
129	4	42
130	4	44
131	4	41
132	4	38
133	4	39
134	4	33
135	4	35
136	4	37
137	4	36
138	4	34
139	4	29
140	4	32
141	4	30
142	4	26
143	4	31
144	4	28
145	4	27
146	4	45
147	4	46
148	4	25
149	4	22
150	4	24
151	4	23
152	4	98
153	4	103
154	4	105
155	4	104
156	4	70
157	4	69
158	4	77
159	4	74
160	4	71
161	4	73
162	4	75
163	4	76
164	4	72
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 164, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Puede crear log entry	1	crear_logentry
2	Puede modificar log entry	1	modificar_logentry
3	Puede eliminar log entry	1	eliminar_logentry
4	Puede crear permission	2	crear_permission
5	Puede modificar permission	2	modificar_permission
6	Puede eliminar permission	2	eliminar_permission
7	Puede crear group	3	crear_group
8	Puede modificar group	3	modificar_group
9	Puede eliminar group	3	eliminar_group
10	Puede crear user	4	crear_user
11	Puede modificar user	4	modificar_user
12	Puede eliminar user	4	eliminar_user
13	Puede crear content type	5	crear_contenttype
14	Puede modificar content type	5	modificar_contenttype
15	Puede eliminar content type	5	eliminar_contenttype
16	Puede crear session	6	crear_session
17	Puede modificar session	6	modificar_session
18	Puede eliminar session	6	eliminar_session
19	Puede crear cron job log	7	crear_cronjoblog
20	Puede modificar cron job log	7	modificar_cronjoblog
21	Puede eliminar cron job log	7	eliminar_cronjoblog
22	Puede crear usuarios	8	crear_usuarios
23	Puede modificar usuarios	8	modificar_usuarios
24	Puede eliminar usuarios	8	eliminar_usuarios
25	puede listar usuarios	8	administrar_usuario
26	Puede crear roles	9	crear_roles
27	Puede modificar roles	9	modificar_roles
28	Puede eliminar roles	9	eliminar_roles
29	puede listar los roles	9	administrar_roles
30	puede asignar un rol a un usuario	9	asignar_rol
31	puede desasignar un rol de un usuario	9	desasignar_rol
32	puede asignar un proyecto a un rol	9	asignar_proyecto_rol
33	Puede crear proyectos	10	crear_proyectos
34	Puede modificar proyectos	10	modificar_proyectos
35	Puede eliminar proyectos	10	eliminar_proyectos
36	Puede listar los miembros de un proyecto	10	listar_miembros
37	Puede importar proyectos	10	importar_proyectos
38	Puede consultar proyectos	10	consultar_proyectos
39	Puede consultar proyectos finalizados	10	consultar_proyectosfinalizados
40	Puede crear fases	11	crear_fases
41	Puede modificar fases	11	modificar_fases
42	Puede eliminar fases	11	eliminar_fases
43	puede listar las Fases	11	administrar_fases
44	puede importar fases	11	importar_fase
45	Puede crear tipo atributo	12	crear_tipoatributo
46	Puede modificar tipo atributo	12	modificar_tipoatributo
47	Puede eliminar tipo atributo	12	eliminar_tipoatributo
48	puede listar los tipos de atributo	12	administrar_tipos_de_atributo
49	puede importar un tipo de atributo	12	importar_tipo_de_atributo
50	Puede crear numerico	13	crear_numerico
51	Puede modificar numerico	13	modificar_numerico
52	Puede eliminar numerico	13	eliminar_numerico
53	Puede crear fecha	14	crear_fecha
54	Puede modificar fecha	14	modificar_fecha
55	Puede eliminar fecha	14	eliminar_fecha
56	Puede crear texto	15	crear_texto
57	Puede modificar texto	15	modificar_texto
58	Puede eliminar texto	15	eliminar_texto
59	Puede crear logico	16	crear_logico
60	Puede modificar logico	16	modificar_logico
61	Puede eliminar logico	16	eliminar_logico
62	Puede crear archivo externo	17	crear_archivoexterno
63	Puede modificar archivo externo	17	modificar_archivoexterno
64	Puede eliminar archivo externo	17	eliminar_archivoexterno
65	Puede crear imagen	18	crear_imagen
66	Puede modificar imagen	18	modificar_imagen
67	Puede eliminar imagen	18	eliminar_imagen
68	Puede crear lista atributo	19	crear_listaatributo
69	Puede modificar lista atributo	19	modificar_listaatributo
70	Puede eliminar lista atributo	19	eliminar_listaatributo
71	Puede crear tipo item	20	crear_tipoitem
72	Puede modificar tipo item	20	modificar_tipoitem
73	Puede eliminar tipo item	20	eliminar_tipoitem
74	Puede consultar los datos de un Tipo de Item	20	consultar_tipoitem
75	Puede gestionar un Tipo de Item	20	gestionar_tipoitem
76	Puede Importar un Tipo de Item	20	importar_tipoitem
77	Puede administrar los Tipos de Item	20	administrar_tipoitem
78	Puede crear items	21	crear_items
79	Puede modificar items	21	modificar_items
80	Puede eliminar items	21	eliminar_items
81	Puede crear valor item	22	crear_valoritem
82	Puede modificar valor item	22	modificar_valoritem
83	Puede eliminar valor item	22	eliminar_valoritem
84	Puede crear lista valores	23	crear_listavalores
85	Puede modificar lista valores	23	modificar_listavalores
86	Puede eliminar lista valores	23	eliminar_listavalores
87	Puede crear relaciones	24	crear_relaciones
88	Puede modificar relaciones	24	modificar_relaciones
89	Puede eliminar relaciones	24	eliminar_relaciones
90	Puede crear linea base	25	crear_lineabase
91	Puede modificar linea base	25	modificar_lineabase
92	Puede eliminar linea base	25	eliminar_lineabase
93	puede listar las Lineas Base	25	administrar_lineas_base
94	puede generar Linea Base	25	generar_linea_base
95	puede generar informe de Linea Base	25	generar_informe_linea_base
96	puede consultar datos de linea base Linea Base	25	consultar_linea_base
97	Puede crear solicitudes	26	crear_solicitudes
98	Puede modificar solicitudes	26	modificar_solicitudes
99	Puede eliminar solicitudes	26	eliminar_solicitudes
100	Puede crear credenciales	27	crear_credenciales
101	Puede modificar credenciales	27	modificar_credenciales
102	Puede eliminar credenciales	27	eliminar_credenciales
103	Puede crear votos	28	crear_votos
104	Puede modificar votos	28	modificar_votos
105	Puede eliminar votos	28	eliminar_votos
106	Puede crear comite	29	crear_comite
107	Puede modificar comite	29	modificar_comite
108	Puede eliminar comite	29	eliminar_comite
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_permission_id_seq', 108, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$12000$4ItH6aDKjvwT$l1yJ2YpUKjDHJyVqI/q2ZqJBgGV6AkPkkrDc8dJxAiU=	2014-06-07 02:38:32.50144-04	t	sap				t	t	2014-06-07 02:37:27.892924-04
3	pbkdf2_sha256$12000$VJzqftNpt0q2$2VTGJ17Jg0hw2MP7xtBc+o3LuUh6dg0RgH5Bflp9+QQ=	2014-06-07 02:39:29.482071-04	f	marcelo	ysapy	ortiz	marce@sap	f	t	2014-06-07 02:39:29.482071-04
5	pbkdf2_sha256$12000$rFURMHdoMEh2$5wp5s0RRahoftBq5FsS5SVL25mwAmGw+5dEjf+JqAL8=	2014-06-07 02:40:27.992253-04	f	usuario1	ysapy	ortiz	usuario1@sap	f	t	2014-06-07 02:40:27.992253-04
6	pbkdf2_sha256$12000$bVxc0kk18YMX$iSX3vhS3Y2DLSrd617i36Zbs2gb09Y7e2NKCoOw6TYg=	2014-06-07 02:40:48.509592-04	f	usuario2	ysapy	ortiz	usuario1@sap	f	t	2014-06-07 02:40:48.509592-04
7	pbkdf2_sha256$12000$CDIxuY6kaBZf$ZTsthhj2d7qnmE/G8tz+p2/8ug/wuU4AVrFrOJxuYNo=	2014-06-07 02:41:04.824345-04	f	usuario3	ysapy	ortiz	usuario1@sap	f	t	2014-06-07 02:41:04.824345-04
4	pbkdf2_sha256$12000$CIK1SNElrBcK$rY+bqGoOzWenZnO1kAyh1feC/Jqr0oRtjbRDxX5OPpY=	2014-06-07 03:14:36.067658-04	f	eduardo	ysapy	ortiz	usuario1@sap	f	t	2014-06-07 02:40:09.012051-04
2	pbkdf2_sha256$12000$9NgvPRLtbwLb$7fKpzV3gj4JUhhEAq66Yjv5XMiZcSYRfssChEmogFoY=	2014-06-07 03:15:07.393009-04	f	ysapy	ysapy	ortiz	usuario1@sap	f	t	2014-06-07 02:38:52.618174-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
2	2	2
3	4	2
4	3	2
5	5	2
6	2	3
7	3	3
8	4	3
9	6	3
10	2	4
11	3	4
12	4	4
13	7	4
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 13, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_id_seq', 7, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: comite_comite; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY comite_comite (id, nombre, proyecto_id) FROM stdin;
1	\N	1
2	\N	2
3	\N	3
\.


--
-- Name: comite_comite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('comite_comite_id_seq', 3, true);


--
-- Data for Name: comite_comite_miembros; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY comite_comite_miembros (id, comite_id, usuarios_id) FROM stdin;
1	2	3
2	2	4
3	2	2
4	3	3
5	3	2
6	3	4
\.


--
-- Name: comite_comite_miembros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('comite_comite_miembros_id_seq', 6, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	cron job log	django_cron	cronjoblog
8	usuarios	usuarios	usuarios
9	roles	roles	roles
10	proyectos	proyectos	proyectos
11	fases	fases	fases
12	tipo atributo	tipoatributo	tipoatributo
13	numerico	tipoatributo	numerico
14	fecha	tipoatributo	fecha
15	texto	tipoatributo	texto
16	logico	tipoatributo	logico
17	archivo externo	tipoatributo	archivoexterno
18	imagen	tipoatributo	imagen
19	lista atributo	tipoitem	listaatributo
20	tipo item	tipoitem	tipoitem
21	items	items	items
22	valor item	items	valoritem
23	lista valores	items	listavalores
24	relaciones	relaciones	relaciones
25	linea base	lineabase	lineabase
26	solicitudes	solicitudes	solicitudes
27	credenciales	solicitudes	credenciales
28	votos	solicitudes	votos
29	comite	comite	comite
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('django_content_type_id_seq', 29, true);


--
-- Data for Name: django_cron_cronjoblog; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_cron_cronjoblog (id, code, start_time, end_time, is_success, message, ran_at_time) FROM stdin;
\.


--
-- Name: django_cron_cronjoblog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('django_cron_cronjoblog_id_seq', 1, false);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
d8iw1j1kgapymzz5osgixhid7tdmrt7x	ZTVhODExMDk3MDI5MTRiNmNmZGYzOWUyNWYxZTFmM2I4NzljODZlNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-21 03:15:07.404596-04
\.


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY fases_fases (id, nombre, nombre_eliminado, descripcion, estado, fechainicio, duracion, proyecto_id, is_active, orden) FROM stdin;
1	Fase 1	\N	Fase 4 del proyecto 1	DR	2014-06-07	16	2	t	1
2	Fase 2	\N	Fase 2 del proyecto 1	DR	2014-06-07	36	2	t	2
3	Fase 3	\N	Fase 1 del proyecto 1	DR	2014-06-07	16	2	t	3
4	Fase 1	\N	Fase 4 del proyecto 1	FD	2014-06-07	8	3	t	1
5	Fase 2	\N	Fase 4 del proyecto 1	FD	2014-06-07	6	3	t	2
6	Fase 3	\N	Fase 4 del proyecto 1	DR	2014-06-07	5	3	t	3
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('fases_fases_id_seq', 6, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_items (id, nombre, version, prioridad, estado, descripcion, observaciones, "costoMonetario", "costoTemporal", complejidad, fase_id, proyecto_id, is_active, tipo_item_id, padre, lb) FROM stdin;
15	item223	2	2	Bloqueado	Fase 4 del proyecto 1	ninguna	2	2	2	5	3	t	2	14	\N
2	item212	1	2	Bloqueado	Fase 4 del proyecto 1	ninguna	2	3	4	1	2	t	1	0	\N
1	item112	1	2	Bloqueado	Fase 4 del proyecto 1	ninguna	2	3	3	1	2	t	1	0	\N
3	item312	1	5	Bloqueado	Fase 4 del proyecto 1	ninguna	4	2	2	1	2	t	1	0	\N
7	item422	1	2	En Construccion	Fase 4 del proyecto 1	ninguna	2	2	3	2	2	t	1	0	\N
5	item222	2	3	Bloqueado	Fase 4 del proyecto 1	ninguna	4	3	3	2	2	t	1	4	\N
4	item122	2	5	Bloqueado	Fase 4 del proyecto 1	ninguna	2	3	4	2	2	t	1	1	\N
6	item322	2	4	Validado	Fase 4 del proyecto 1	ninguna	2	2	1	2	2	t	1	4	\N
9	item232	1	2	En Construccion	Fase 4 del proyecto 1	ninguna	2	2	2	3	2	t	1	0	\N
16	item133	2	2	Bloqueado	Fase 4 del proyecto 1	ninguna	2	3	2	6	3	t	2	14	\N
10	item332	2	3	En Construccion	Fase 4 del proyecto 1	btip	4	2	3	3	2	t	1	9	\N
8	item132	2	3	En Construccion	Fase 4 del proyecto 1	ninguna	2	2	2	3	2	t	1	4	\N
17	item233	2	1	Bloqueado	Fase 4 del proyecto 1	ninguna	2	2	2	6	3	t	2	15	\N
18	item333	2	2	Bloqueado	Fase 4 del proyecto 1	ninguna	2	2	2	6	3	t	2	15	\N
12	item213	1	3	Bloqueado	Fase 4 del proyecto 1	ninguna	2	3	2	4	3	t	2	0	\N
11	item113	1	2	Bloqueado	Fase 4 del proyecto 1	ninguna	1	4	3	4	3	t	2	0	\N
13	item313	1	2	Bloqueado	Fase 4 del proyecto 1	ninguna	2	2	2	4	3	t	2	0	\N
14	item123	2	3	Bloqueado	Fase 4 del proyecto 1	ninguna	2	2	2	5	3	t	2	11	\N
\.


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_items_id_seq', 18, true);


--
-- Data for Name: items_listavalores; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_listavalores (id, nombre, nombre_atributo, tipo_dato, valor_texto, valor_numerico, valor_fecha, valor_archivoexterno, valor_imagen, orden) FROM stdin;
\.


--
-- Name: items_listavalores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_listavalores_id_seq', 1, false);


--
-- Data for Name: items_valoritem; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_valoritem (id, nombre, item_id, valor_id, tabla_valor_nombre, nombre_atributo, tipo_dato, version, orden, fase_id, proyecto_id) FROM stdin;
\.


--
-- Name: items_valoritem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_valoritem_id_seq', 1, false);


--
-- Data for Name: lineabase_lineabase; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY lineabase_lineabase (id, numero, proyecto_id, fase_id, is_active, descripcion, fecha_creacion) FROM stdin;
1	1	2	1	t		2014-06-07
2	2	2	1	t		2014-06-07
3	1	2	2	t		2014-06-07
4	1	3	4	t		2014-06-07
5	2	3	4	t		2014-06-07
6	1	3	5	t		2014-06-07
7	1	3	6	t		2014-06-07
\.


--
-- Name: lineabase_lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_id_seq', 7, true);


--
-- Data for Name: lineabase_lineabase_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY lineabase_lineabase_items (id, lineabase_id, items_id) FROM stdin;
1	1	2
2	1	1
3	2	3
4	3	5
5	3	4
6	4	12
7	4	11
8	5	13
9	6	14
10	6	15
11	7	16
12	7	17
13	7	18
\.


--
-- Name: lineabase_lineabase_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_items_id_seq', 13, true);


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY proyectos_proyectos (id, nombre, lider_id, estado, fecha_inicio, duracion, is_active) FROM stdin;
1	Proyecto 1	3	Inactivo	2014-04-04	74	t
2	Proyecto 2	2	En Construccion	2014-04-04	53	t
3	Proyecto 3	4	En Construccion	2014-04-04	26	t
\.


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 3, true);


--
-- Data for Name: relaciones_relaciones; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY relaciones_relaciones (id, nombre, padre_id, item, version) FROM stdin;
1	\N	1	4	2
2	\N	4	5	2
3	\N	4	6	2
4	\N	9	10	2
5	\N	4	8	2
6	\N	11	14	2
7	\N	14	15	2
8	\N	14	16	2
9	\N	15	17	2
10	\N	15	18	2
11	\N	15	18	2
\.


--
-- Name: relaciones_relaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('relaciones_relaciones_id_seq', 11, true);


--
-- Data for Name: roles_roles; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY roles_roles (group_ptr_id, proyecto, descripcion, is_active) FROM stdin;
1			t
2	1		t
3	2		t
4	3		t
\.


--
-- Data for Name: roles_roles_fases; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY roles_roles_fases (id, roles_id, fases_id) FROM stdin;
\.


--
-- Name: roles_roles_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('roles_roles_fases_id_seq', 1, false);


--
-- Data for Name: solicitudes_credenciales; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_credenciales (id, nombre, usuario_id, proyecto_id, fase_id, item_id, fecha_aprobacion, fecha_expiracion, estado, observaciones) FROM stdin;
\.


--
-- Name: solicitudes_credenciales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_credenciales_id_seq', 1, false);


--
-- Data for Name: solicitudes_solicitudes; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_solicitudes (id, nombre, usuario_id, proyecto_id, fase_id, item_id, fecha_solicitud, tiempo_solicitado, descripcion, observaciones, estado, tiempo_esperado) FROM stdin;
1	\N	2	2	1	1	2014-06-07	8	se necesita cargar atributos	ninguna	Pendiente	2
\.


--
-- Name: solicitudes_solicitudes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_solicitudes_id_seq', 1, true);


--
-- Data for Name: solicitudes_votos; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_votos (id, miembro_id, solicitud_id, "fechaDeVotacion", voto) FROM stdin;
\.


--
-- Name: solicitudes_votos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_votos_id_seq', 1, false);


--
-- Data for Name: tipoatributo_archivoexterno; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_archivoexterno (id, valor, id_item, nombre_atributo, obligatorio) FROM stdin;
\.


--
-- Name: tipoatributo_archivoexterno_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_archivoexterno_id_seq', 1, false);


--
-- Data for Name: tipoatributo_fecha; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_fecha (id, valor, id_item, nombre_atributo, obligatorio) FROM stdin;
\.


--
-- Name: tipoatributo_fecha_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_fecha_id_seq', 1, false);


--
-- Data for Name: tipoatributo_imagen; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_imagen (id, valor, id_item, nombre_atributo, obligatorio) FROM stdin;
\.


--
-- Name: tipoatributo_imagen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_imagen_id_seq', 1, false);


--
-- Data for Name: tipoatributo_logico; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_logico (id, valor, id_item, nombre_atributo, obligatorio) FROM stdin;
\.


--
-- Name: tipoatributo_logico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_logico_id_seq', 1, false);


--
-- Data for Name: tipoatributo_numerico; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_numerico (id, valor, id_item, nombre_atributo, "precision", longitud, obligatorio) FROM stdin;
\.


--
-- Name: tipoatributo_numerico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_numerico_id_seq', 1, false);


--
-- Data for Name: tipoatributo_texto; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_texto (id, valor, id_item, nombre_atributo, longitud, obligatorio) FROM stdin;
\.


--
-- Name: tipoatributo_texto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_texto_id_seq', 1, false);


--
-- Data for Name: tipoatributo_tipoatributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_tipoatributo (id, nombre, tipo, "precision", longitud, obligatorio, descripcion, is_active) FROM stdin;
1	cantidad	Numerico	2	3	f		t
\.


--
-- Name: tipoatributo_tipoatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_id_seq', 1, true);


--
-- Data for Name: tipoatributo_tipoatributo_proyecto; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_tipoatributo_proyecto (id, tipoatributo_id, proyectos_id) FROM stdin;
1	1	2
2	1	3
\.


--
-- Name: tipoatributo_tipoatributo_proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_proyecto_id_seq', 2, true);


--
-- Data for Name: tipoitem_listaatributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_listaatributo (id, id_atributo, id_tipoitem, orden, nombre, is_active) FROM stdin;
1	1	1	1	cantidad	t
2	1	1	2	cantidad	t
3	1	2	1	cantidad	t
\.


--
-- Name: tipoitem_listaatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_listaatributo_id_seq', 3, true);


--
-- Data for Name: tipoitem_tipoitem; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_tipoitem (id, nombre, descripcion, id_proyecto, is_active) FROM stdin;
1	Requerimiento	REQUERIMIENTOS 	2	t
2	Desarrollo	DESARROLLO	3	t
\.


--
-- Name: tipoitem_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_tipoitem_id_seq', 2, true);


--
-- Data for Name: tipoitem_tipoitem_listaAtributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY "tipoitem_tipoitem_listaAtributo" (id, tipoitem_id, listaatributo_id) FROM stdin;
1	1	1
2	1	2
3	2	3
\.


--
-- Name: tipoitem_tipoitem_listaAtributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('"tipoitem_tipoitem_listaAtributo_id_seq"', 3, true);


--
-- Data for Name: usuarios_usuarios; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY usuarios_usuarios (user_id, telefono, direccion, especialidad, observaciones) FROM stdin;
1				
2	021	lambare	desarrollador	ninguna
3	021	lambare	desarrollador	ninguna
4	j	lambare	desarrollador	ninguna
5	021	lambare	desarrollador	ninguna
6	021	k	desarrollador	ninguna
7	021	lambare	desarrollador	ninguna
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: comite_comite_miembros_comite_id_usuarios_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY comite_comite_miembros
    ADD CONSTRAINT comite_comite_miembros_comite_id_usuarios_id_key UNIQUE (comite_id, usuarios_id);


--
-- Name: comite_comite_miembros_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY comite_comite_miembros
    ADD CONSTRAINT comite_comite_miembros_pkey PRIMARY KEY (id);


--
-- Name: comite_comite_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY comite_comite
    ADD CONSTRAINT comite_comite_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_cron_cronjoblog_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY django_cron_cronjoblog
    ADD CONSTRAINT django_cron_cronjoblog_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: fases_fases_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY fases_fases
    ADD CONSTRAINT fases_fases_pkey PRIMARY KEY (id);


--
-- Name: items_items_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY items_items
    ADD CONSTRAINT items_items_pkey PRIMARY KEY (id);


--
-- Name: items_listavalores_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY items_listavalores
    ADD CONSTRAINT items_listavalores_pkey PRIMARY KEY (id);


--
-- Name: items_valoritem_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY items_valoritem
    ADD CONSTRAINT items_valoritem_pkey PRIMARY KEY (id);


--
-- Name: lineabase_lineabase_items_lineabase_id_items_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY lineabase_lineabase_items
    ADD CONSTRAINT lineabase_lineabase_items_lineabase_id_items_id_key UNIQUE (lineabase_id, items_id);


--
-- Name: lineabase_lineabase_items_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY lineabase_lineabase_items
    ADD CONSTRAINT lineabase_lineabase_items_pkey PRIMARY KEY (id);


--
-- Name: lineabase_lineabase_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY lineabase_lineabase
    ADD CONSTRAINT lineabase_lineabase_pkey PRIMARY KEY (id);


--
-- Name: proyectos_proyectos_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY proyectos_proyectos
    ADD CONSTRAINT proyectos_proyectos_pkey PRIMARY KEY (id);


--
-- Name: relaciones_relaciones_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY relaciones_relaciones
    ADD CONSTRAINT relaciones_relaciones_pkey PRIMARY KEY (id);


--
-- Name: roles_roles_fases_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY roles_roles_fases
    ADD CONSTRAINT roles_roles_fases_pkey PRIMARY KEY (id);


--
-- Name: roles_roles_fases_roles_id_fases_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY roles_roles_fases
    ADD CONSTRAINT roles_roles_fases_roles_id_fases_id_key UNIQUE (roles_id, fases_id);


--
-- Name: roles_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY roles_roles
    ADD CONSTRAINT roles_roles_pkey PRIMARY KEY (group_ptr_id);


--
-- Name: solicitudes_credenciales_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY solicitudes_credenciales
    ADD CONSTRAINT solicitudes_credenciales_pkey PRIMARY KEY (id);


--
-- Name: solicitudes_solicitudes_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_pkey PRIMARY KEY (id);


--
-- Name: solicitudes_votos_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY solicitudes_votos
    ADD CONSTRAINT solicitudes_votos_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_archivoexterno_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_archivoexterno
    ADD CONSTRAINT tipoatributo_archivoexterno_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_fecha_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_fecha
    ADD CONSTRAINT tipoatributo_fecha_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_imagen_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_imagen
    ADD CONSTRAINT tipoatributo_imagen_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_logico_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_logico
    ADD CONSTRAINT tipoatributo_logico_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_numerico_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_numerico
    ADD CONSTRAINT tipoatributo_numerico_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_texto_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_texto
    ADD CONSTRAINT tipoatributo_texto_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_tipoatributo_nombre_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_tipoatributo
    ADD CONSTRAINT tipoatributo_tipoatributo_nombre_key UNIQUE (nombre);


--
-- Name: tipoatributo_tipoatributo_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_tipoatributo
    ADD CONSTRAINT tipoatributo_tipoatributo_pkey PRIMARY KEY (id);


--
-- Name: tipoatributo_tipoatributo_proy_tipoatributo_id_proyectos_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_tipoatributo_proyecto
    ADD CONSTRAINT tipoatributo_tipoatributo_proy_tipoatributo_id_proyectos_id_key UNIQUE (tipoatributo_id, proyectos_id);


--
-- Name: tipoatributo_tipoatributo_proyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoatributo_tipoatributo_proyecto
    ADD CONSTRAINT tipoatributo_tipoatributo_proyecto_pkey PRIMARY KEY (id);


--
-- Name: tipoitem_listaatributo_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoitem_listaatributo
    ADD CONSTRAINT tipoitem_listaatributo_pkey PRIMARY KEY (id);


--
-- Name: tipoitem_tipoitem_listaAtribut_tipoitem_id_listaatributo_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY "tipoitem_tipoitem_listaAtributo"
    ADD CONSTRAINT "tipoitem_tipoitem_listaAtribut_tipoitem_id_listaatributo_id_key" UNIQUE (tipoitem_id, listaatributo_id);


--
-- Name: tipoitem_tipoitem_listaAtributo_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY "tipoitem_tipoitem_listaAtributo"
    ADD CONSTRAINT "tipoitem_tipoitem_listaAtributo_pkey" PRIMARY KEY (id);


--
-- Name: tipoitem_tipoitem_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY tipoitem_tipoitem
    ADD CONSTRAINT tipoitem_tipoitem_pkey PRIMARY KEY (id);


--
-- Name: usuarios_usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY usuarios_usuarios
    ADD CONSTRAINT usuarios_usuarios_pkey PRIMARY KEY (user_id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: comite_comite_miembros_comite_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX comite_comite_miembros_comite_id ON comite_comite_miembros USING btree (comite_id);


--
-- Name: comite_comite_miembros_usuarios_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX comite_comite_miembros_usuarios_id ON comite_comite_miembros USING btree (usuarios_id);


--
-- Name: comite_comite_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX comite_comite_proyecto_id ON comite_comite USING btree (proyecto_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_cron_cronjoblog_1fe0e40b; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_1fe0e40b ON django_cron_cronjoblog USING btree (code, start_time, ran_at_time);


--
-- Name: django_cron_cronjoblog_495fb183; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_495fb183 ON django_cron_cronjoblog USING btree (code, start_time);


--
-- Name: django_cron_cronjoblog_63e2740d; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_63e2740d ON django_cron_cronjoblog USING btree (code, is_success, ran_at_time);


--
-- Name: django_cron_cronjoblog_code; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_code ON django_cron_cronjoblog USING btree (code);


--
-- Name: django_cron_cronjoblog_code_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_code_like ON django_cron_cronjoblog USING btree (code varchar_pattern_ops);


--
-- Name: django_cron_cronjoblog_end_time; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_end_time ON django_cron_cronjoblog USING btree (end_time);


--
-- Name: django_cron_cronjoblog_ran_at_time; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_ran_at_time ON django_cron_cronjoblog USING btree (ran_at_time);


--
-- Name: django_cron_cronjoblog_start_time; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_cron_cronjoblog_start_time ON django_cron_cronjoblog USING btree (start_time);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: fases_fases_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX fases_fases_proyecto_id ON fases_fases USING btree (proyecto_id);


--
-- Name: items_items_fase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX items_items_fase_id ON items_items USING btree (fase_id);


--
-- Name: items_items_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX items_items_proyecto_id ON items_items USING btree (proyecto_id);


--
-- Name: items_items_tipo_item_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX items_items_tipo_item_id ON items_items USING btree (tipo_item_id);


--
-- Name: items_valoritem_fase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX items_valoritem_fase_id ON items_valoritem USING btree (fase_id);


--
-- Name: items_valoritem_item_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX items_valoritem_item_id ON items_valoritem USING btree (item_id);


--
-- Name: items_valoritem_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX items_valoritem_proyecto_id ON items_valoritem USING btree (proyecto_id);


--
-- Name: lineabase_lineabase_fase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX lineabase_lineabase_fase_id ON lineabase_lineabase USING btree (fase_id);


--
-- Name: lineabase_lineabase_items_items_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX lineabase_lineabase_items_items_id ON lineabase_lineabase_items USING btree (items_id);


--
-- Name: lineabase_lineabase_items_lineabase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX lineabase_lineabase_items_lineabase_id ON lineabase_lineabase_items USING btree (lineabase_id);


--
-- Name: lineabase_lineabase_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX lineabase_lineabase_proyecto_id ON lineabase_lineabase USING btree (proyecto_id);


--
-- Name: proyectos_proyectos_lider_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX proyectos_proyectos_lider_id ON proyectos_proyectos USING btree (lider_id);


--
-- Name: relaciones_relaciones_padre_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX relaciones_relaciones_padre_id ON relaciones_relaciones USING btree (padre_id);


--
-- Name: roles_roles_fases_fases_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX roles_roles_fases_fases_id ON roles_roles_fases USING btree (fases_id);


--
-- Name: roles_roles_fases_roles_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX roles_roles_fases_roles_id ON roles_roles_fases USING btree (roles_id);


--
-- Name: solicitudes_credenciales_fase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_credenciales_fase_id ON solicitudes_credenciales USING btree (fase_id);


--
-- Name: solicitudes_credenciales_item_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_credenciales_item_id ON solicitudes_credenciales USING btree (item_id);


--
-- Name: solicitudes_credenciales_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_credenciales_proyecto_id ON solicitudes_credenciales USING btree (proyecto_id);


--
-- Name: solicitudes_credenciales_usuario_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_credenciales_usuario_id ON solicitudes_credenciales USING btree (usuario_id);


--
-- Name: solicitudes_solicitudes_fase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_fase_id ON solicitudes_solicitudes USING btree (fase_id);


--
-- Name: solicitudes_solicitudes_item_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_item_id ON solicitudes_solicitudes USING btree (item_id);


--
-- Name: solicitudes_solicitudes_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_proyecto_id ON solicitudes_solicitudes USING btree (proyecto_id);


--
-- Name: solicitudes_solicitudes_usuario_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_usuario_id ON solicitudes_solicitudes USING btree (usuario_id);


--
-- Name: solicitudes_votos_miembro_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_votos_miembro_id ON solicitudes_votos USING btree (miembro_id);


--
-- Name: solicitudes_votos_solicitud_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_votos_solicitud_id ON solicitudes_votos USING btree (solicitud_id);


--
-- Name: tipoatributo_tipoatributo_nombre_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX tipoatributo_tipoatributo_nombre_like ON tipoatributo_tipoatributo USING btree (nombre varchar_pattern_ops);


--
-- Name: tipoatributo_tipoatributo_proyecto_proyectos_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX tipoatributo_tipoatributo_proyecto_proyectos_id ON tipoatributo_tipoatributo_proyecto USING btree (proyectos_id);


--
-- Name: tipoatributo_tipoatributo_proyecto_tipoatributo_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX tipoatributo_tipoatributo_proyecto_tipoatributo_id ON tipoatributo_tipoatributo_proyecto USING btree (tipoatributo_id);


--
-- Name: tipoitem_tipoitem_listaAtributo_listaatributo_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX "tipoitem_tipoitem_listaAtributo_listaatributo_id" ON "tipoitem_tipoitem_listaAtributo" USING btree (listaatributo_id);


--
-- Name: tipoitem_tipoitem_listaAtributo_tipoitem_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX "tipoitem_tipoitem_listaAtributo_tipoitem_id" ON "tipoitem_tipoitem_listaAtributo" USING btree (tipoitem_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comite_comite_miembros_usuarios_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY comite_comite_miembros
    ADD CONSTRAINT comite_comite_miembros_usuarios_id_fkey FOREIGN KEY (usuarios_id) REFERENCES usuarios_usuarios(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comite_comite_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY comite_comite
    ADD CONSTRAINT comite_comite_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: comite_id_refs_id_b93ed40d; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY comite_comite_miembros
    ADD CONSTRAINT comite_id_refs_id_b93ed40d FOREIGN KEY (comite_id) REFERENCES comite_comite(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_93d2d1f8; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT content_type_id_refs_id_93d2d1f8 FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fases_fases_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY fases_fases
    ADD CONSTRAINT fases_fases_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fases_id_refs_id_f013efc7; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY roles_roles_fases
    ADD CONSTRAINT fases_id_refs_id_f013efc7 FOREIGN KEY (fases_id) REFERENCES fases_fases(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: items_items_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_items
    ADD CONSTRAINT items_items_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fases_fases(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: items_items_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_items
    ADD CONSTRAINT items_items_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: items_items_tipo_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_items
    ADD CONSTRAINT items_items_tipo_item_id_fkey FOREIGN KEY (tipo_item_id) REFERENCES tipoitem_tipoitem(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: items_valoritem_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_valoritem
    ADD CONSTRAINT items_valoritem_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fases_fases(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: items_valoritem_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_valoritem
    ADD CONSTRAINT items_valoritem_item_id_fkey FOREIGN KEY (item_id) REFERENCES items_items(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: items_valoritem_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY items_valoritem
    ADD CONSTRAINT items_valoritem_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lineabase_id_refs_id_398bc2f5; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY lineabase_lineabase_items
    ADD CONSTRAINT lineabase_id_refs_id_398bc2f5 FOREIGN KEY (lineabase_id) REFERENCES lineabase_lineabase(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lineabase_lineabase_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY lineabase_lineabase
    ADD CONSTRAINT lineabase_lineabase_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fases_fases(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lineabase_lineabase_items_items_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY lineabase_lineabase_items
    ADD CONSTRAINT lineabase_lineabase_items_items_id_fkey FOREIGN KEY (items_id) REFERENCES items_items(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: lineabase_lineabase_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY lineabase_lineabase
    ADD CONSTRAINT lineabase_lineabase_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyectos_proyectos_lider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY proyectos_proyectos
    ADD CONSTRAINT proyectos_proyectos_lider_id_fkey FOREIGN KEY (lider_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: relaciones_relaciones_padre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY relaciones_relaciones
    ADD CONSTRAINT relaciones_relaciones_padre_id_fkey FOREIGN KEY (padre_id) REFERENCES items_items(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: roles_id_refs_group_ptr_id_11e17ff0; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY roles_roles_fases
    ADD CONSTRAINT roles_id_refs_group_ptr_id_11e17ff0 FOREIGN KEY (roles_id) REFERENCES roles_roles(group_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: roles_roles_group_ptr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY roles_roles
    ADD CONSTRAINT roles_roles_group_ptr_id_fkey FOREIGN KEY (group_ptr_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_credenciales_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_credenciales
    ADD CONSTRAINT solicitudes_credenciales_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fases_fases(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_credenciales_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_credenciales
    ADD CONSTRAINT solicitudes_credenciales_item_id_fkey FOREIGN KEY (item_id) REFERENCES items_items(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_credenciales_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_credenciales
    ADD CONSTRAINT solicitudes_credenciales_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_credenciales_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_credenciales
    ADD CONSTRAINT solicitudes_credenciales_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuarios_usuarios(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_solicitudes_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fases_fases(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_solicitudes_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_item_id_fkey FOREIGN KEY (item_id) REFERENCES items_items(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_solicitudes_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_solicitudes_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuarios_usuarios(user_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_votos_miembro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_votos
    ADD CONSTRAINT solicitudes_votos_miembro_id_fkey FOREIGN KEY (miembro_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_votos_solicitud_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_votos
    ADD CONSTRAINT solicitudes_votos_solicitud_id_fkey FOREIGN KEY (solicitud_id) REFERENCES solicitudes_solicitudes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoatributo_id_refs_id_58907e1e; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_tipoatributo_proyecto
    ADD CONSTRAINT tipoatributo_id_refs_id_58907e1e FOREIGN KEY (tipoatributo_id) REFERENCES tipoatributo_tipoatributo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoatributo_tipoatributo_proyecto_proyectos_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY tipoatributo_tipoatributo_proyecto
    ADD CONSTRAINT tipoatributo_tipoatributo_proyecto_proyectos_id_fkey FOREIGN KEY (proyectos_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoitem_id_refs_id_e4d37b53; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY "tipoitem_tipoitem_listaAtributo"
    ADD CONSTRAINT tipoitem_id_refs_id_e4d37b53 FOREIGN KEY (tipoitem_id) REFERENCES tipoitem_tipoitem(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tipoitem_tipoitem_listaAtributo_listaatributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY "tipoitem_tipoitem_listaAtributo"
    ADD CONSTRAINT "tipoitem_tipoitem_listaAtributo_listaatributo_id_fkey" FOREIGN KEY (listaatributo_id) REFERENCES tipoitem_listaatributo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_c0d12874; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT user_id_refs_id_c0d12874 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: usuarios_usuarios_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY usuarios_usuarios
    ADD CONSTRAINT usuarios_usuarios_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

