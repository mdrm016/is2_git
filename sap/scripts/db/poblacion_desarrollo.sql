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
ALTER TABLE ONLY public.djcelery_taskstate DROP CONSTRAINT djcelery_taskstate_worker_id_fkey;
ALTER TABLE ONLY public.djcelery_periodictask DROP CONSTRAINT djcelery_periodictask_interval_id_fkey;
ALTER TABLE ONLY public.djcelery_periodictask DROP CONSTRAINT djcelery_periodictask_crontab_id_fkey;
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
DROP INDEX public.djcelery_workerstate_last_heartbeat;
DROP INDEX public.djcelery_workerstate_hostname_like;
DROP INDEX public.djcelery_taskstate_worker_id;
DROP INDEX public.djcelery_taskstate_tstamp;
DROP INDEX public.djcelery_taskstate_task_id_like;
DROP INDEX public.djcelery_taskstate_state_like;
DROP INDEX public.djcelery_taskstate_state;
DROP INDEX public.djcelery_taskstate_name_like;
DROP INDEX public.djcelery_taskstate_name;
DROP INDEX public.djcelery_taskstate_hidden;
DROP INDEX public.djcelery_periodictask_name_like;
DROP INDEX public.djcelery_periodictask_interval_id;
DROP INDEX public.djcelery_periodictask_crontab_id;
DROP INDEX public.django_session_session_key_like;
DROP INDEX public.django_session_expire_date;
DROP INDEX public.django_admin_log_user_id;
DROP INDEX public.django_admin_log_content_type_id;
DROP INDEX public.comite_comite_proyecto_id;
DROP INDEX public.comite_comite_miembros_usuarios_id;
DROP INDEX public.comite_comite_miembros_comite_id;
DROP INDEX public.celery_tasksetmeta_taskset_id_like;
DROP INDEX public.celery_tasksetmeta_hidden;
DROP INDEX public.celery_taskmeta_task_id_like;
DROP INDEX public.celery_taskmeta_hidden;
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
ALTER TABLE ONLY public.djcelery_workerstate DROP CONSTRAINT djcelery_workerstate_pkey;
ALTER TABLE ONLY public.djcelery_workerstate DROP CONSTRAINT djcelery_workerstate_hostname_key;
ALTER TABLE ONLY public.djcelery_taskstate DROP CONSTRAINT djcelery_taskstate_task_id_key;
ALTER TABLE ONLY public.djcelery_taskstate DROP CONSTRAINT djcelery_taskstate_pkey;
ALTER TABLE ONLY public.djcelery_periodictasks DROP CONSTRAINT djcelery_periodictasks_pkey;
ALTER TABLE ONLY public.djcelery_periodictask DROP CONSTRAINT djcelery_periodictask_pkey;
ALTER TABLE ONLY public.djcelery_periodictask DROP CONSTRAINT djcelery_periodictask_name_key;
ALTER TABLE ONLY public.djcelery_intervalschedule DROP CONSTRAINT djcelery_intervalschedule_pkey;
ALTER TABLE ONLY public.djcelery_crontabschedule DROP CONSTRAINT djcelery_crontabschedule_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_key;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.comite_comite DROP CONSTRAINT comite_comite_pkey;
ALTER TABLE ONLY public.comite_comite_miembros DROP CONSTRAINT comite_comite_miembros_pkey;
ALTER TABLE ONLY public.comite_comite_miembros DROP CONSTRAINT comite_comite_miembros_comite_id_usuarios_id_key;
ALTER TABLE ONLY public.celery_tasksetmeta DROP CONSTRAINT celery_tasksetmeta_taskset_id_key;
ALTER TABLE ONLY public.celery_tasksetmeta DROP CONSTRAINT celery_tasksetmeta_pkey;
ALTER TABLE ONLY public.celery_taskmeta DROP CONSTRAINT celery_taskmeta_task_id_key;
ALTER TABLE ONLY public.celery_taskmeta DROP CONSTRAINT celery_taskmeta_pkey;
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
ALTER TABLE public.djcelery_workerstate ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.djcelery_taskstate ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.djcelery_periodictask ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.djcelery_intervalschedule ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.djcelery_crontabschedule ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.comite_comite_miembros ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.comite_comite ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.celery_tasksetmeta ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.celery_taskmeta ALTER COLUMN id DROP DEFAULT;
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
DROP SEQUENCE public.djcelery_workerstate_id_seq;
DROP TABLE public.djcelery_workerstate;
DROP SEQUENCE public.djcelery_taskstate_id_seq;
DROP TABLE public.djcelery_taskstate;
DROP TABLE public.djcelery_periodictasks;
DROP SEQUENCE public.djcelery_periodictask_id_seq;
DROP TABLE public.djcelery_periodictask;
DROP SEQUENCE public.djcelery_intervalschedule_id_seq;
DROP TABLE public.djcelery_intervalschedule;
DROP SEQUENCE public.djcelery_crontabschedule_id_seq;
DROP TABLE public.djcelery_crontabschedule;
DROP TABLE public.django_session;
DROP SEQUENCE public.django_content_type_id_seq;
DROP TABLE public.django_content_type;
DROP SEQUENCE public.django_admin_log_id_seq;
DROP TABLE public.django_admin_log;
DROP SEQUENCE public.comite_comite_miembros_id_seq;
DROP TABLE public.comite_comite_miembros;
DROP SEQUENCE public.comite_comite_id_seq;
DROP TABLE public.comite_comite;
DROP SEQUENCE public.celery_tasksetmeta_id_seq;
DROP TABLE public.celery_tasksetmeta;
DROP SEQUENCE public.celery_taskmeta_id_seq;
DROP TABLE public.celery_taskmeta;
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
-- Name: celery_taskmeta; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE celery_taskmeta (
    id integer NOT NULL,
    task_id character varying(255) NOT NULL,
    status character varying(50) NOT NULL,
    result text,
    date_done timestamp with time zone NOT NULL,
    traceback text,
    hidden boolean NOT NULL,
    meta text
);


ALTER TABLE public.celery_taskmeta OWNER TO sap;

--
-- Name: celery_taskmeta_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE celery_taskmeta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.celery_taskmeta_id_seq OWNER TO sap;

--
-- Name: celery_taskmeta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE celery_taskmeta_id_seq OWNED BY celery_taskmeta.id;


--
-- Name: celery_tasksetmeta; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE celery_tasksetmeta (
    id integer NOT NULL,
    taskset_id character varying(255) NOT NULL,
    result text NOT NULL,
    date_done timestamp with time zone NOT NULL,
    hidden boolean NOT NULL
);


ALTER TABLE public.celery_tasksetmeta OWNER TO sap;

--
-- Name: celery_tasksetmeta_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE celery_tasksetmeta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.celery_tasksetmeta_id_seq OWNER TO sap;

--
-- Name: celery_tasksetmeta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE celery_tasksetmeta_id_seq OWNED BY celery_tasksetmeta.id;


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
-- Name: django_session; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO sap;

--
-- Name: djcelery_crontabschedule; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE djcelery_crontabschedule (
    id integer NOT NULL,
    minute character varying(64) NOT NULL,
    hour character varying(64) NOT NULL,
    day_of_week character varying(64) NOT NULL,
    day_of_month character varying(64) NOT NULL,
    month_of_year character varying(64) NOT NULL
);


ALTER TABLE public.djcelery_crontabschedule OWNER TO sap;

--
-- Name: djcelery_crontabschedule_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE djcelery_crontabschedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.djcelery_crontabschedule_id_seq OWNER TO sap;

--
-- Name: djcelery_crontabschedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE djcelery_crontabschedule_id_seq OWNED BY djcelery_crontabschedule.id;


--
-- Name: djcelery_intervalschedule; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE djcelery_intervalschedule (
    id integer NOT NULL,
    every integer NOT NULL,
    period character varying(24) NOT NULL
);


ALTER TABLE public.djcelery_intervalschedule OWNER TO sap;

--
-- Name: djcelery_intervalschedule_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE djcelery_intervalschedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.djcelery_intervalschedule_id_seq OWNER TO sap;

--
-- Name: djcelery_intervalschedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE djcelery_intervalschedule_id_seq OWNED BY djcelery_intervalschedule.id;


--
-- Name: djcelery_periodictask; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE djcelery_periodictask (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    task character varying(200) NOT NULL,
    interval_id integer,
    crontab_id integer,
    args text NOT NULL,
    kwargs text NOT NULL,
    queue character varying(200),
    exchange character varying(200),
    routing_key character varying(200),
    expires timestamp with time zone,
    enabled boolean NOT NULL,
    last_run_at timestamp with time zone,
    total_run_count integer NOT NULL,
    date_changed timestamp with time zone NOT NULL,
    description text NOT NULL,
    CONSTRAINT djcelery_periodictask_total_run_count_check CHECK ((total_run_count >= 0))
);


ALTER TABLE public.djcelery_periodictask OWNER TO sap;

--
-- Name: djcelery_periodictask_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE djcelery_periodictask_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.djcelery_periodictask_id_seq OWNER TO sap;

--
-- Name: djcelery_periodictask_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE djcelery_periodictask_id_seq OWNED BY djcelery_periodictask.id;


--
-- Name: djcelery_periodictasks; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE djcelery_periodictasks (
    ident smallint NOT NULL,
    last_update timestamp with time zone NOT NULL
);


ALTER TABLE public.djcelery_periodictasks OWNER TO sap;

--
-- Name: djcelery_taskstate; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE djcelery_taskstate (
    id integer NOT NULL,
    state character varying(64) NOT NULL,
    task_id character varying(36) NOT NULL,
    name character varying(200),
    tstamp timestamp with time zone NOT NULL,
    args text,
    kwargs text,
    eta timestamp with time zone,
    expires timestamp with time zone,
    result text,
    traceback text,
    runtime double precision,
    retries integer NOT NULL,
    worker_id integer,
    hidden boolean NOT NULL
);


ALTER TABLE public.djcelery_taskstate OWNER TO sap;

--
-- Name: djcelery_taskstate_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE djcelery_taskstate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.djcelery_taskstate_id_seq OWNER TO sap;

--
-- Name: djcelery_taskstate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE djcelery_taskstate_id_seq OWNED BY djcelery_taskstate.id;


--
-- Name: djcelery_workerstate; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE djcelery_workerstate (
    id integer NOT NULL,
    hostname character varying(255) NOT NULL,
    last_heartbeat timestamp with time zone
);


ALTER TABLE public.djcelery_workerstate OWNER TO sap;

--
-- Name: djcelery_workerstate_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE djcelery_workerstate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.djcelery_workerstate_id_seq OWNER TO sap;

--
-- Name: djcelery_workerstate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE djcelery_workerstate_id_seq OWNED BY djcelery_workerstate.id;


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
    version integer,
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

ALTER TABLE ONLY celery_taskmeta ALTER COLUMN id SET DEFAULT nextval('celery_taskmeta_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY celery_tasksetmeta ALTER COLUMN id SET DEFAULT nextval('celery_tasksetmeta_id_seq'::regclass);


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

ALTER TABLE ONLY djcelery_crontabschedule ALTER COLUMN id SET DEFAULT nextval('djcelery_crontabschedule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_intervalschedule ALTER COLUMN id SET DEFAULT nextval('djcelery_intervalschedule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_periodictask ALTER COLUMN id SET DEFAULT nextval('djcelery_periodictask_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_taskstate ALTER COLUMN id SET DEFAULT nextval('djcelery_taskstate_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_workerstate ALTER COLUMN id SET DEFAULT nextval('djcelery_workerstate_id_seq'::regclass);


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
2	P2
3	P3
1	P1
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_id_seq', 3, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
66	2	28
67	2	30
68	2	29
69	2	25
70	2	27
71	2	26
72	2	34
73	2	36
74	2	35
75	2	31
76	2	33
77	2	32
78	2	19
79	2	21
80	2	20
81	2	22
82	2	24
83	2	23
84	2	40
85	2	42
86	2	41
87	2	37
88	2	39
89	2	38
90	2	46
91	2	43
92	2	45
93	2	44
94	2	119
95	2	124
96	2	126
97	2	125
98	2	83
99	2	85
100	2	84
101	2	74
102	2	76
103	2	75
104	2	86
105	2	88
106	2	87
107	2	80
108	2	82
109	2	81
110	2	71
111	2	73
112	2	72
113	2	77
114	2	79
115	2	78
116	2	69
117	2	66
118	2	68
119	2	70
120	2	67
121	2	89
122	2	91
123	2	90
124	2	98
125	2	95
126	2	92
127	2	94
128	2	96
129	2	97
130	2	93
131	3	28
132	3	30
133	3	29
134	3	25
135	3	27
136	3	26
137	3	34
138	3	36
139	3	35
140	3	31
141	3	33
142	3	32
143	3	19
144	3	21
145	3	20
146	3	22
147	3	24
148	3	23
149	3	40
150	3	42
151	3	41
152	3	37
153	3	39
154	3	38
155	3	46
156	3	43
157	3	45
158	3	44
159	3	119
160	3	124
161	3	126
162	3	125
163	3	83
164	3	85
165	3	84
166	3	74
167	3	76
168	3	75
169	3	86
170	3	88
171	3	87
172	3	80
173	3	82
174	3	81
175	3	71
176	3	73
177	3	72
178	3	77
179	3	79
180	3	78
181	3	69
182	3	66
183	3	68
184	3	70
185	3	67
186	3	89
187	3	91
188	3	90
189	3	98
190	3	95
191	3	92
192	3	94
193	3	96
194	3	97
195	3	93
196	1	28
197	1	30
198	1	29
199	1	25
200	1	27
201	1	26
202	1	34
203	1	36
204	1	35
205	1	31
206	1	33
207	1	32
208	1	19
209	1	21
210	1	20
211	1	22
212	1	24
213	1	23
214	1	40
215	1	42
216	1	41
217	1	37
218	1	39
219	1	38
220	1	43
221	1	44
222	1	119
223	1	124
224	1	126
225	1	125
226	1	83
227	1	85
228	1	84
229	1	74
230	1	76
231	1	75
232	1	86
233	1	88
234	1	87
235	1	80
236	1	82
237	1	81
238	1	71
239	1	73
240	1	72
241	1	77
242	1	79
243	1	78
244	1	69
245	1	66
246	1	68
247	1	70
248	1	67
249	1	89
250	1	91
251	1	90
252	1	98
253	1	95
254	1	92
255	1	96
256	1	97
257	1	93
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 257, true);


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
19	Puede crear task state	7	crear_taskmeta
20	Puede modificar task state	7	modificar_taskmeta
21	Puede eliminar task state	7	eliminar_taskmeta
22	Puede crear saved group result	8	crear_tasksetmeta
23	Puede modificar saved group result	8	modificar_tasksetmeta
24	Puede eliminar saved group result	8	eliminar_tasksetmeta
25	Puede crear interval	9	crear_intervalschedule
26	Puede modificar interval	9	modificar_intervalschedule
27	Puede eliminar interval	9	eliminar_intervalschedule
28	Puede crear crontab	10	crear_crontabschedule
29	Puede modificar crontab	10	modificar_crontabschedule
30	Puede eliminar crontab	10	eliminar_crontabschedule
31	Puede crear periodic tasks	11	crear_periodictasks
32	Puede modificar periodic tasks	11	modificar_periodictasks
33	Puede eliminar periodic tasks	11	eliminar_periodictasks
34	Puede crear periodic task	12	crear_periodictask
35	Puede modificar periodic task	12	modificar_periodictask
36	Puede eliminar periodic task	12	eliminar_periodictask
37	Puede crear worker	13	crear_workerstate
38	Puede modificar worker	13	modificar_workerstate
39	Puede eliminar worker	13	eliminar_workerstate
40	Puede crear task	14	crear_taskstate
41	Puede modificar task	14	modificar_taskstate
42	Puede eliminar task	14	eliminar_taskstate
43	Puede crear usuarios	15	crear_usuarios
44	Puede modificar usuarios	15	modificar_usuarios
45	Puede eliminar usuarios	15	eliminar_usuarios
46	puede listar usuarios	15	administrar_usuario
47	Puede crear roles	16	crear_roles
48	Puede modificar roles	16	modificar_roles
49	Puede eliminar roles	16	eliminar_roles
50	puede listar los roles	16	administrar_roles
51	puede asignar un rol a un usuario	16	asignar_rol
52	puede desasignar un rol de un usuario	16	desasignar_rol
53	puede asignar un proyecto a un rol	16	asignar_proyecto_rol
54	Puede crear proyectos	17	crear_proyectos
55	Puede modificar proyectos	17	modificar_proyectos
56	Puede eliminar proyectos	17	eliminar_proyectos
57	Puede listar los miembros de un proyecto	17	listar_miembros
58	Puede importar proyectos	17	importar_proyectos
59	Puede consultar proyectos	17	consultar_proyectos
60	Puede consultar proyectos finalizados	17	consultar_proyectosfinalizados
61	Puede crear fases	18	crear_fases
62	Puede modificar fases	18	modificar_fases
63	Puede eliminar fases	18	eliminar_fases
64	puede listar las Fases	18	administrar_fases
65	puede importar fases	18	importar_fase
66	Puede crear tipo atributo	19	crear_tipoatributo
67	Puede modificar tipo atributo	19	modificar_tipoatributo
68	Puede eliminar tipo atributo	19	eliminar_tipoatributo
69	puede listar los tipos de atributo	19	administrar_tipos_de_atributo
70	puede importar un tipo de atributo	19	importar_tipo_de_atributo
71	Puede crear numerico	20	crear_numerico
72	Puede modificar numerico	20	modificar_numerico
73	Puede eliminar numerico	20	eliminar_numerico
74	Puede crear fecha	21	crear_fecha
75	Puede modificar fecha	21	modificar_fecha
76	Puede eliminar fecha	21	eliminar_fecha
77	Puede crear texto	22	crear_texto
78	Puede modificar texto	22	modificar_texto
79	Puede eliminar texto	22	eliminar_texto
80	Puede crear logico	23	crear_logico
81	Puede modificar logico	23	modificar_logico
82	Puede eliminar logico	23	eliminar_logico
83	Puede crear archivo externo	24	crear_archivoexterno
84	Puede modificar archivo externo	24	modificar_archivoexterno
85	Puede eliminar archivo externo	24	eliminar_archivoexterno
86	Puede crear imagen	25	crear_imagen
87	Puede modificar imagen	25	modificar_imagen
88	Puede eliminar imagen	25	eliminar_imagen
89	Puede crear lista atributo	26	crear_listaatributo
90	Puede modificar lista atributo	26	modificar_listaatributo
91	Puede eliminar lista atributo	26	eliminar_listaatributo
92	Puede crear tipo item	27	crear_tipoitem
93	Puede modificar tipo item	27	modificar_tipoitem
94	Puede eliminar tipo item	27	eliminar_tipoitem
95	Puede consultar los datos de un Tipo de Item	27	consultar_tipoitem
96	Puede gestionar un Tipo de Item	27	gestionar_tipoitem
97	Puede Importar un Tipo de Item	27	importar_tipoitem
98	Puede administrar los Tipos de Item	27	administrar_tipoitem
99	Puede crear items	28	crear_items
100	Puede modificar items	28	modificar_items
101	Puede eliminar items	28	eliminar_items
102	Puede crear valor item	29	crear_valoritem
103	Puede modificar valor item	29	modificar_valoritem
104	Puede eliminar valor item	29	eliminar_valoritem
105	Puede crear lista valores	30	crear_listavalores
106	Puede modificar lista valores	30	modificar_listavalores
107	Puede eliminar lista valores	30	eliminar_listavalores
108	Puede crear relaciones	31	crear_relaciones
109	Puede modificar relaciones	31	modificar_relaciones
110	Puede eliminar relaciones	31	eliminar_relaciones
111	Puede crear linea base	32	crear_lineabase
112	Puede modificar linea base	32	modificar_lineabase
113	Puede eliminar linea base	32	eliminar_lineabase
114	puede listar las Lineas Base	32	administrar_lineas_base
115	puede generar Linea Base	32	generar_linea_base
116	puede generar informe de Linea Base	32	generar_informe_linea_base
117	puede consultar datos de linea base Linea Base	32	consultar_linea_base
118	Puede crear solicitudes	33	crear_solicitudes
119	Puede modificar solicitudes	33	modificar_solicitudes
120	Puede eliminar solicitudes	33	eliminar_solicitudes
121	Puede crear credenciales	34	crear_credenciales
122	Puede modificar credenciales	34	modificar_credenciales
123	Puede eliminar credenciales	34	eliminar_credenciales
124	Puede crear votos	35	crear_votos
125	Puede modificar votos	35	modificar_votos
126	Puede eliminar votos	35	eliminar_votos
127	Puede crear comite	36	crear_comite
128	Puede modificar comite	36	modificar_comite
129	Puede eliminar comite	36	eliminar_comite
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_permission_id_seq', 129, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$12000$HaBJktpC6cRj$v6bRZ/YkBUNfmj/ZTRmjOVDtaHeuvrF1VTlv52zsaoc=	2014-06-19 23:45:54.793979-04	t	sap				t	t	2014-06-19 23:44:15.028777-04
5	pbkdf2_sha256$12000$v7QMODqFyApu$Nl5a9HSzXM3c9VaAbd0mXDceRPKkACMlyn2UG9cwIHc=	2014-06-19 23:51:09.285529-04	f	usuario1	ysapy	ortiz	usuario1@sap	f	t	2014-06-19 23:51:09.285529-04
6	pbkdf2_sha256$12000$eAEcFj0ZCTbd$ozLLtv7DLwqii05zazhuJhvt+n95ZPcS2eSa9bzZWjo=	2014-06-19 23:51:39.317142-04	f	usuario2	ysapy	ortiz	usuario1@sap	f	t	2014-06-19 23:51:39.317142-04
7	pbkdf2_sha256$12000$gk3Zb4ieXyYM$BmiNpldTKwx8v7U6zrVmWQp6q2haw28aBDseO/RfUvM=	2014-06-19 23:52:10.972536-04	f	usuario3	ysapy	ortiz	usuario1@sap	f	t	2014-06-19 23:52:10.972536-04
3	pbkdf2_sha256$12000$orl093mknDGU$0l4HCQovbW1zw6Uz5tYAB0+XS/1C0cffdzfeOtSNzxs=	2014-06-20 03:10:06.661939-04	f	marcelo	ysapy	ortiz	usuario1@sap	f	t	2014-06-19 23:46:38.590652-04
4	pbkdf2_sha256$12000$79btee1mxCvo$jtEMaFDMG3rAUoYNR2+3ctTkYXMbdDsvHVZBiuD7dzk=	2014-06-20 03:10:40.199025-04	f	eduardo	ysapy	ortiz	edu@sap	f	t	2014-06-19 23:48:55.045541-04
2	pbkdf2_sha256$12000$rNtI6MgEiC0h$7mhiCrG/mbOmQKC/51k2kXIpSQbCCswDnUOMQBODbCw=	2014-06-20 18:50:37.718648-04	f	ysapy	ysapy	j	usuario1@sap	f	t	2014-06-19 23:46:19.818572-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
2	2	1
3	3	1
4	4	1
5	5	1
6	6	1
7	7	1
9	2	2
10	3	2
11	4	2
12	5	2
13	6	2
14	7	2
16	2	3
17	3	3
18	4	3
19	5	3
20	6	3
21	7	3
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 21, true);


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
-- Data for Name: celery_taskmeta; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY celery_taskmeta (id, task_id, status, result, date_done, traceback, hidden, meta) FROM stdin;
\.


--
-- Name: celery_taskmeta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('celery_taskmeta_id_seq', 1, false);


--
-- Data for Name: celery_tasksetmeta; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY celery_tasksetmeta (id, taskset_id, result, date_done, hidden) FROM stdin;
\.


--
-- Name: celery_tasksetmeta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('celery_tasksetmeta_id_seq', 1, false);


--
-- Data for Name: comite_comite; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY comite_comite (id, nombre, proyecto_id) FROM stdin;
1	\N	1
3	\N	3
2	\N	2
\.


--
-- Name: comite_comite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('comite_comite_id_seq', 3, true);


--
-- Data for Name: comite_comite_miembros; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY comite_comite_miembros (id, comite_id, usuarios_id) FROM stdin;
10	3	3
11	3	2
12	3	4
16	2	3
17	2	4
18	2	2
\.


--
-- Name: comite_comite_miembros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('comite_comite_miembros_id_seq', 18, true);


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
7	task state	djcelery	taskmeta
8	saved group result	djcelery	tasksetmeta
9	interval	djcelery	intervalschedule
10	crontab	djcelery	crontabschedule
11	periodic tasks	djcelery	periodictasks
12	periodic task	djcelery	periodictask
13	worker	djcelery	workerstate
14	task	djcelery	taskstate
15	usuarios	usuarios	usuarios
16	roles	roles	roles
17	proyectos	proyectos	proyectos
18	fases	fases	fases
19	tipo atributo	tipoatributo	tipoatributo
20	numerico	tipoatributo	numerico
21	fecha	tipoatributo	fecha
22	texto	tipoatributo	texto
23	logico	tipoatributo	logico
24	archivo externo	tipoatributo	archivoexterno
25	imagen	tipoatributo	imagen
26	lista atributo	tipoitem	listaatributo
27	tipo item	tipoitem	tipoitem
28	items	items	items
29	valor item	items	valoritem
30	lista valores	items	listavalores
31	relaciones	relaciones	relaciones
32	linea base	lineabase	lineabase
33	solicitudes	solicitudes	solicitudes
34	credenciales	solicitudes	credenciales
35	votos	solicitudes	votos
36	comite	comite	comite
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('django_content_type_id_seq', 36, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
uoofuagxrxkbx17pggfc58jvl9kgoqv5	YTJiMmNhZGI5ZjRjNGM5M2FkNGE5NTRmNDc3OWM5YmNlN2M0MTczOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=	2014-07-04 02:12:54.013556-04
rzry1gsxcb36ue2u4b1e7fgianx6c50p	ZTVhODExMDk3MDI5MTRiNmNmZGYzOWUyNWYxZTFmM2I4NzljODZlNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-07-04 03:22:58.286211-04
vhst6ov4ro79mlt88royqosl64ynj47d	ZTVhODExMDk3MDI5MTRiNmNmZGYzOWUyNWYxZTFmM2I4NzljODZlNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-07-04 18:50:37.763753-04
\.


--
-- Data for Name: djcelery_crontabschedule; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY djcelery_crontabschedule (id, minute, hour, day_of_week, day_of_month, month_of_year) FROM stdin;
\.


--
-- Name: djcelery_crontabschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('djcelery_crontabschedule_id_seq', 1, false);


--
-- Data for Name: djcelery_intervalschedule; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY djcelery_intervalschedule (id, every, period) FROM stdin;
\.


--
-- Name: djcelery_intervalschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('djcelery_intervalschedule_id_seq', 1, false);


--
-- Data for Name: djcelery_periodictask; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY djcelery_periodictask (id, name, task, interval_id, crontab_id, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description) FROM stdin;
\.


--
-- Name: djcelery_periodictask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('djcelery_periodictask_id_seq', 1, false);


--
-- Data for Name: djcelery_periodictasks; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY djcelery_periodictasks (ident, last_update) FROM stdin;
\.


--
-- Data for Name: djcelery_taskstate; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY djcelery_taskstate (id, state, task_id, name, tstamp, args, kwargs, eta, expires, result, traceback, runtime, retries, worker_id, hidden) FROM stdin;
\.


--
-- Name: djcelery_taskstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('djcelery_taskstate_id_seq', 1, false);


--
-- Data for Name: djcelery_workerstate; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY djcelery_workerstate (id, hostname, last_heartbeat) FROM stdin;
\.


--
-- Name: djcelery_workerstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('djcelery_workerstate_id_seq', 1, false);


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY fases_fases (id, nombre, nombre_eliminado, descripcion, estado, fechainicio, duracion, proyecto_id, is_active, orden) FROM stdin;
2	F2	\N	Fase 2 del proyecto 2	DR	2014-06-20	32	2	t	2
1	F1	\N	Fase 1 del Proyecto 2	FD	2014-06-20	14	2	t	1
3	F3	\N	Fase 3 del proyecto 2	DR	2014-06-20	11	2	t	3
4	F4	\N	Fase 4 del proyecto 2	DR	2014-06-20	9	2	t	4
5	F1	\N	Fase 1 del proyecto 3	FD	2014-06-20	14	3	t	1
6	F2	\N	fase 2 del proyecto 3	FD	2014-06-20	7	3	t	2
7	F3	\N	fase 3 del proyecto 3	FD	2014-06-20	5	3	t	3
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('fases_fases_id_seq', 7, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_items (id, nombre, version, prioridad, estado, descripcion, observaciones, "costoMonetario", "costoTemporal", complejidad, fase_id, proyecto_id, is_active, tipo_item_id, padre, lb) FROM stdin;
3	item312	1	7	Bloqueado	item 3, fase 1, proyecto 2	ninguna	75000	36	6	1	2	t	1	0	3
2	item212	1	5	En Revision	item 2, fase1, proyecto 2	ninguna	20000	11	4	1	2	t	2	0	2
8	item232	2	8	En Revision	item 2, fase 3, proyecto 2	ninguna	45000	9	9	3	2	t	1	7	7
7	item132	3	5	En Revision	item 1, fase 3, proyecto 2	ninguna	10000	8	5	3	2	t	2	4	7
5	item222	2	6	En Revision	item 2, fase 2, proyecto 2	ninguna	15000	6	4	2	2	t	1	4	5
4	item122	4	3	En Revision	item 1, fase 2, proyecto 2	ninguna	25000	16	5	2	2	t	2	1	4
11	item242	2	3	En Revision	item 2, fase 4, proyecto 2	ninguna	20000	4	4	4	2	t	2	10	8
10	item142	2	4	En Revision	item 1, fase 4, proyecto 2	ninguna	10000	3	4	4	2	t	2	9	8
9	item332	2	10	En Revision	item 3, fase 3, proyecto 2	ninguna	30000	13	7	3	2	t	2	6	7
6	item322	2	5	En Revision	item 3, fase 2, proyecto 2	ninguna	30000	3	4	2	2	t	2	1	6
1	item112	12	4	Habilitado	item 1, fase 1, proyecto 2	ninguna	40000	9	4	1	2	t	2	0	1
13	item213	1	6	En Revision	item 2, fase 1, proyecto 3	ninguna	12	4	6	5	3	t	3	0	9
15	item223	2	3	En Revision	item 2, fase 2, proyecto 3	ninguna	4	4	4	6	3	t	3	14	10
16	item133	2	3	En Revision	item 1, fase 3, proyecto 3	ninguna	5	7	6	7	3	t	3	14	11
14	item123	2	3	En Revision	item 1, fase 2, proyecto 3	ninguna	5	5	4	6	3	t	3	12	10
12	item113	1	9	Habilitado	item 1, fase 1, proyecto 3	ninguna	5	5	3	5	3	t	3	0	9
\.


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_items_id_seq', 16, true);


--
-- Data for Name: items_listavalores; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_listavalores (id, nombre, nombre_atributo, tipo_dato, valor_texto, valor_numerico, valor_fecha, valor_archivoexterno, valor_imagen, orden) FROM stdin;
1	\N	nombre	Texto	planeamiento 1	\N	\N			1
2	\N	temporal	Logico	\N	\N	\N			2
3	\N	nombre	Texto	planeamiento	\N	\N			1
4	\N	temporal	Logico	\N	\N	\N			2
5	\N	nombre	Texto	planeamiento	\N	\N			1
6	\N	temporal	Logico	\N	\N	\N			2
7	\N	nombre	Texto	planeamiento 1	\N	\N			1
8	\N	temporal	Logico	\N	\N	\N			2
9	\N	nombre	Texto	planeamiento 1	\N	\N			1
10	\N	temporal	Logico	\N	\N	\N			2
11	\N	nombre	Texto	planeamiento 1	\N	\N			1
12	\N	temporal	Logico	\N	\N	\N			2
13	\N	nombre	Texto	planeamiento 1	\N	\N			1
14	\N	temporal	Logico	\N	\N	\N			2
15	\N	nombre	Texto	planeamiento 1	\N	\N			1
16	\N	temporal	Logico	\N	\N	\N			2
17	\N	nombre	Texto	planeamiento 1	\N	\N			1
18	\N	temporal	Logico	\N	\N	\N			2
19	\N	nombre	Texto	planeamiento 1	\N	\N			1
20	\N	temporal	Logico	\N	\N	\N			2
21	\N	nombre	Texto	planeamiento 1	\N	\N			1
22	\N	temporal	Logico	\N	\N	\N			2
\.


--
-- Name: items_listavalores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_listavalores_id_seq', 22, true);


--
-- Data for Name: items_valoritem; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_valoritem (id, nombre, item_id, valor_id, tabla_valor_nombre, nombre_atributo, tipo_dato, version, orden, fase_id, proyecto_id) FROM stdin;
1	\N	1	1	tipoatributo_texto	nombre	Texto	2	1	1	2
2	\N	1	1	tipoatributo_logico	temporal	Logico	2	2	1	2
3	\N	1	2	tipoatributo_texto	nombre	Texto	3	1	1	2
4	\N	1	2	tipoatributo_logico	temporal	Logico	3	2	1	2
5	\N	1	3	tipoatributo_texto	nombre	Texto	4	1	1	2
6	\N	1	3	tipoatributo_logico	temporal	Logico	4	2	1	2
7	\N	1	4	tipoatributo_texto	nombre	Texto	5	1	1	2
8	\N	1	4	tipoatributo_logico	temporal	Logico	5	2	1	2
9	\N	1	5	tipoatributo_texto	nombre	Texto	6	1	1	2
10	\N	1	5	tipoatributo_logico	temporal	Logico	6	2	1	2
11	\N	1	6	tipoatributo_texto	nombre	Texto	7	1	1	2
12	\N	1	6	tipoatributo_logico	temporal	Logico	7	2	1	2
13	\N	1	7	tipoatributo_texto	nombre	Texto	8	1	1	2
14	\N	1	7	tipoatributo_logico	temporal	Logico	8	2	1	2
15	\N	1	8	tipoatributo_texto	nombre	Texto	9	1	1	2
16	\N	1	8	tipoatributo_logico	temporal	Logico	9	2	1	2
17	\N	1	9	tipoatributo_texto	nombre	Texto	10	1	1	2
18	\N	1	9	tipoatributo_logico	temporal	Logico	10	2	1	2
19	\N	1	10	tipoatributo_texto	nombre	Texto	11	1	1	2
20	\N	1	10	tipoatributo_logico	temporal	Logico	11	2	1	2
21	\N	1	11	tipoatributo_texto	nombre	Texto	12	1	1	2
22	\N	1	11	tipoatributo_logico	temporal	Logico	12	2	1	2
23	\N	7	12	tipoatributo_texto	nombre	Texto	3	1	3	2
24	\N	7	12	tipoatributo_logico	temporal	Logico	3	2	3	2
\.


--
-- Name: items_valoritem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_valoritem_id_seq', 24, true);


--
-- Data for Name: lineabase_lineabase; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY lineabase_lineabase (id, numero, proyecto_id, fase_id, is_active, descripcion, fecha_creacion) FROM stdin;
3	2	2	1	t	Con item 312	2014-06-20
4	1	2	2	t	item 1	2014-06-20
5	2	2	2	t	item 2	2014-06-20
6	3	2	2	t	item 3	2014-06-20
7	1	2	3	t	los 3 de fase 3	2014-06-20
8	1	2	4	t	unico de fase 4	2014-06-20
10	1	3	6	t	fase 2 proyecto 3	2014-06-20
11	1	3	7	t	proyecto 3 fase 3	2014-06-20
1	1	2	1	f	Linea base Proyecto 2 fase 1	2014-06-20
9	1	3	5	f	los dos	2014-06-20
\.


--
-- Name: lineabase_lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_id_seq', 11, true);


--
-- Data for Name: lineabase_lineabase_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY lineabase_lineabase_items (id, lineabase_id, items_id) FROM stdin;
1	1	2
2	1	1
5	3	3
6	4	4
7	5	5
8	6	6
9	7	7
10	7	8
11	7	9
12	8	10
13	8	11
14	9	12
15	9	13
16	10	14
17	10	15
18	11	16
\.


--
-- Name: lineabase_lineabase_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_items_id_seq', 18, true);


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY proyectos_proyectos (id, nombre, lider_id, estado, fecha_inicio, duracion, is_active) FROM stdin;
1	P1	3	Inactivo	2014-05-16	32	t
2	P2	2	En Construccion	2014-05-16	22	t
3	P3	4	En Construccion	2014-05-16	48	t
\.


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 3, true);


--
-- Data for Name: relaciones_relaciones; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY relaciones_relaciones (id, nombre, padre_id, item, version) FROM stdin;
1	\N	2	1	5
2	\N	2	1	7
3	\N	2	1	10
4	\N	2	1	11
5	\N	1	4	2
6	\N	4	5	2
7	\N	1	6	2
8	\N	1	4	4
9	\N	4	7	2
10	\N	7	8	2
11	\N	6	9	2
12	\N	4	7	3
13	\N	10	11	2
14	\N	9	10	2
15	\N	12	14	2
16	\N	14	15	2
17	\N	14	16	2
\.


--
-- Name: relaciones_relaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('relaciones_relaciones_id_seq', 17, true);


--
-- Data for Name: roles_roles; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY roles_roles (group_ptr_id, proyecto, descripcion, is_active) FROM stdin;
2	2		t
3	3		t
1	1		t
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

COPY solicitudes_credenciales (id, nombre, usuario_id, proyecto_id, fase_id, item_id, version, fecha_aprobacion, fecha_expiracion, estado, observaciones) FROM stdin;
1	\N	2	2	1	1	12	2014-06-20	2014-06-28	Habilitado	\N
2	\N	2	3	5	12	1	2014-06-20	2014-06-28	Habilitado	\N
\.


--
-- Name: solicitudes_credenciales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_credenciales_id_seq', 2, true);


--
-- Data for Name: solicitudes_solicitudes; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_solicitudes (id, nombre, usuario_id, proyecto_id, fase_id, item_id, fecha_solicitud, tiempo_solicitado, descripcion, observaciones, estado, tiempo_esperado) FROM stdin;
1	\N	2	2	1	1	2014-06-20	8	se necesita cargar atributos	ninguna	Aprobada	2
2	\N	2	3	5	12	2014-06-20	8	Fase 7 del proyecto 2	ninguna	Aprobada	4
3	\N	2	2	1	3	2014-06-20	5	Fase 4 del proyecto 1	ninguna	Pendiente	3
\.


--
-- Name: solicitudes_solicitudes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_solicitudes_id_seq', 3, true);


--
-- Data for Name: solicitudes_votos; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_votos (id, miembro_id, solicitud_id, "fechaDeVotacion", voto) FROM stdin;
1	2	1	2014-06-20	A
2	2	2	2014-06-20	A
3	3	1	2014-06-20	R
4	3	2	2014-06-20	R
5	4	1	2014-06-20	A
6	4	2	2014-06-20	A
\.


--
-- Name: solicitudes_votos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_votos_id_seq', 6, true);


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
1	t	1	temporal	f
2	t	1	temporal	f
3	t	1	temporal	f
4	t	1	temporal	f
5	t	1	temporal	f
6	t	1	temporal	f
7	t	1	temporal	f
8	t	1	temporal	f
9	t	1	temporal	f
10	t	1	temporal	f
11	t	1	temporal	f
12	t	7	temporal	f
\.


--
-- Name: tipoatributo_logico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_logico_id_seq', 12, true);


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
1	planeamiento 1	1	nombre	30	f
2	planeamiento	1	nombre	30	f
3	planeamiento 1	1	nombre	30	f
4	planeamiento 1	1	nombre	30	f
5	planeamiento 1	1	nombre	30	f
6	planeamiento 1	1	nombre	30	f
7	planeamiento 1	1	nombre	30	f
8	planeamiento 1	1	nombre	30	f
9	planeamiento 1	1	nombre	30	f
10	planeamiento 1	1	nombre	30	f
11	planeamiento 1	1	nombre	30	f
12	item 132 inicio	7	nombre	30	f
\.


--
-- Name: tipoatributo_texto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_texto_id_seq', 12, true);


--
-- Data for Name: tipoatributo_tipoatributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_tipoatributo (id, nombre, tipo, "precision", longitud, obligatorio, descripcion, is_active) FROM stdin;
1	cantidad	Numerico	1	3	f		t
2	temporal	Logico	0	0	f		t
3	nombre	Texto	0	30	f		t
\.


--
-- Name: tipoatributo_tipoatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_id_seq', 3, true);


--
-- Data for Name: tipoatributo_tipoatributo_proyecto; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_tipoatributo_proyecto (id, tipoatributo_id, proyectos_id) FROM stdin;
1	1	2
2	2	2
3	3	2
4	1	3
5	3	3
\.


--
-- Name: tipoatributo_tipoatributo_proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_proyecto_id_seq', 5, true);


--
-- Data for Name: tipoitem_listaatributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_listaatributo (id, id_atributo, id_tipoitem, orden, nombre, is_active) FROM stdin;
2	3	1	1	nombre	t
1	1	1	2	cantidad	t
3	3	2	1	nombre	t
4	2	2	2	temporal	t
5	1	3	1	cantidad	t
6	3	3	2	nombre	t
\.


--
-- Name: tipoitem_listaatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_listaatributo_id_seq', 6, true);


--
-- Data for Name: tipoitem_tipoitem; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_tipoitem (id, nombre, descripcion, id_proyecto, is_active) FROM stdin;
1	Requerimiento	Requerimientos del proyecto	2	t
2	Planificacion	Iniciando proyecto	2	t
3	Requerimiento	Requerimientos iniciales	3	t
\.


--
-- Name: tipoitem_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_tipoitem_id_seq', 3, true);


--
-- Data for Name: tipoitem_tipoitem_listaAtributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY "tipoitem_tipoitem_listaAtributo" (id, tipoitem_id, listaatributo_id) FROM stdin;
1	1	1
2	1	2
3	2	3
4	2	4
5	3	5
6	3	6
\.


--
-- Name: tipoitem_tipoitem_listaAtributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('"tipoitem_tipoitem_listaAtributo_id_seq"', 6, true);


--
-- Data for Name: usuarios_usuarios; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY usuarios_usuarios (user_id, telefono, direccion, especialidad, observaciones) FROM stdin;
1				
2	021	lambare	desarrollador	ninguna
3	021	lambare	desarrollador	e un tedyiblilla
4	021	lambare	desarrollador	ninguna
5	021	lambare	desarrollador	j
6	021	lambare	desarrollador	ninguna
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
-- Name: celery_taskmeta_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY celery_taskmeta
    ADD CONSTRAINT celery_taskmeta_pkey PRIMARY KEY (id);


--
-- Name: celery_taskmeta_task_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY celery_taskmeta
    ADD CONSTRAINT celery_taskmeta_task_id_key UNIQUE (task_id);


--
-- Name: celery_tasksetmeta_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY celery_tasksetmeta
    ADD CONSTRAINT celery_tasksetmeta_pkey PRIMARY KEY (id);


--
-- Name: celery_tasksetmeta_taskset_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY celery_tasksetmeta
    ADD CONSTRAINT celery_tasksetmeta_taskset_id_key UNIQUE (taskset_id);


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
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: djcelery_crontabschedule_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_crontabschedule
    ADD CONSTRAINT djcelery_crontabschedule_pkey PRIMARY KEY (id);


--
-- Name: djcelery_intervalschedule_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_intervalschedule
    ADD CONSTRAINT djcelery_intervalschedule_pkey PRIMARY KEY (id);


--
-- Name: djcelery_periodictask_name_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_periodictask
    ADD CONSTRAINT djcelery_periodictask_name_key UNIQUE (name);


--
-- Name: djcelery_periodictask_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_periodictask
    ADD CONSTRAINT djcelery_periodictask_pkey PRIMARY KEY (id);


--
-- Name: djcelery_periodictasks_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_periodictasks
    ADD CONSTRAINT djcelery_periodictasks_pkey PRIMARY KEY (ident);


--
-- Name: djcelery_taskstate_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_taskstate
    ADD CONSTRAINT djcelery_taskstate_pkey PRIMARY KEY (id);


--
-- Name: djcelery_taskstate_task_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_taskstate
    ADD CONSTRAINT djcelery_taskstate_task_id_key UNIQUE (task_id);


--
-- Name: djcelery_workerstate_hostname_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_workerstate
    ADD CONSTRAINT djcelery_workerstate_hostname_key UNIQUE (hostname);


--
-- Name: djcelery_workerstate_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY djcelery_workerstate
    ADD CONSTRAINT djcelery_workerstate_pkey PRIMARY KEY (id);


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
-- Name: celery_taskmeta_hidden; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX celery_taskmeta_hidden ON celery_taskmeta USING btree (hidden);


--
-- Name: celery_taskmeta_task_id_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX celery_taskmeta_task_id_like ON celery_taskmeta USING btree (task_id varchar_pattern_ops);


--
-- Name: celery_tasksetmeta_hidden; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX celery_tasksetmeta_hidden ON celery_tasksetmeta USING btree (hidden);


--
-- Name: celery_tasksetmeta_taskset_id_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX celery_tasksetmeta_taskset_id_like ON celery_tasksetmeta USING btree (taskset_id varchar_pattern_ops);


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
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: djcelery_periodictask_crontab_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_periodictask_crontab_id ON djcelery_periodictask USING btree (crontab_id);


--
-- Name: djcelery_periodictask_interval_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_periodictask_interval_id ON djcelery_periodictask USING btree (interval_id);


--
-- Name: djcelery_periodictask_name_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_periodictask_name_like ON djcelery_periodictask USING btree (name varchar_pattern_ops);


--
-- Name: djcelery_taskstate_hidden; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_hidden ON djcelery_taskstate USING btree (hidden);


--
-- Name: djcelery_taskstate_name; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_name ON djcelery_taskstate USING btree (name);


--
-- Name: djcelery_taskstate_name_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_name_like ON djcelery_taskstate USING btree (name varchar_pattern_ops);


--
-- Name: djcelery_taskstate_state; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_state ON djcelery_taskstate USING btree (state);


--
-- Name: djcelery_taskstate_state_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_state_like ON djcelery_taskstate USING btree (state varchar_pattern_ops);


--
-- Name: djcelery_taskstate_task_id_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_task_id_like ON djcelery_taskstate USING btree (task_id varchar_pattern_ops);


--
-- Name: djcelery_taskstate_tstamp; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_tstamp ON djcelery_taskstate USING btree (tstamp);


--
-- Name: djcelery_taskstate_worker_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_taskstate_worker_id ON djcelery_taskstate USING btree (worker_id);


--
-- Name: djcelery_workerstate_hostname_like; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_workerstate_hostname_like ON djcelery_workerstate USING btree (hostname varchar_pattern_ops);


--
-- Name: djcelery_workerstate_last_heartbeat; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX djcelery_workerstate_last_heartbeat ON djcelery_workerstate USING btree (last_heartbeat);


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
-- Name: djcelery_periodictask_crontab_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_periodictask
    ADD CONSTRAINT djcelery_periodictask_crontab_id_fkey FOREIGN KEY (crontab_id) REFERENCES djcelery_crontabschedule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djcelery_periodictask_interval_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_periodictask
    ADD CONSTRAINT djcelery_periodictask_interval_id_fkey FOREIGN KEY (interval_id) REFERENCES djcelery_intervalschedule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djcelery_taskstate_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY djcelery_taskstate
    ADD CONSTRAINT djcelery_taskstate_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES djcelery_workerstate(id) DEFERRABLE INITIALLY DEFERRED;


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

