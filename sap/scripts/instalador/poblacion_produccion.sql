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
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_usuario_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_proyecto_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes_miembros_que_votaron DROP CONSTRAINT solicitudes_solicitudes_miembros_que_votaron_user_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_item_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_fase_id_fkey;
ALTER TABLE ONLY public.solicitudes_solicitudes_miembros_que_votaron DROP CONSTRAINT solicitudes_id_refs_id_e2c6bdc7;
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
DROP INDEX public.solicitudes_solicitudes_usuario_id;
DROP INDEX public.solicitudes_solicitudes_proyecto_id;
DROP INDEX public.solicitudes_solicitudes_miembros_que_votaron_user_id;
DROP INDEX public.solicitudes_solicitudes_miembros_que_votaron_solicitudes_id;
DROP INDEX public.solicitudes_solicitudes_item_id;
DROP INDEX public.solicitudes_solicitudes_fase_id;
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
ALTER TABLE ONLY public.usuarios_usuarios DROP CONSTRAINT usuarios_usuarios_user_id_key;
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
ALTER TABLE ONLY public.solicitudes_solicitudes DROP CONSTRAINT solicitudes_solicitudes_pkey;
ALTER TABLE ONLY public.solicitudes_solicitudes_miembros_que_votaron DROP CONSTRAINT solicitudes_solicitudes_miembros_que_votaron_pkey;
ALTER TABLE ONLY public.solicitudes_solicitudes_miembros_que_votaron DROP CONSTRAINT solicitudes_solicitudes_miembros_que_solicitudes_id_user_id_key;
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
ALTER TABLE public.usuarios_usuarios ALTER COLUMN id DROP DEFAULT;
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
ALTER TABLE public.solicitudes_solicitudes_miembros_que_votaron ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.solicitudes_solicitudes ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.roles_roles_fases ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.relaciones_relaciones ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.proyectos_proyectos ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.lineabase_lineabase_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.lineabase_lineabase ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_valoritem ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_listavalores ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.fases_fases ALTER COLUMN id DROP DEFAULT;
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
DROP SEQUENCE public.usuarios_usuarios_id_seq;
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
DROP SEQUENCE public.solicitudes_solicitudes_miembros_que_votaron_id_seq;
DROP TABLE public.solicitudes_solicitudes_miembros_que_votaron;
DROP SEQUENCE public.solicitudes_solicitudes_id_seq;
DROP TABLE public.solicitudes_solicitudes;
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
    tiempo_esperado integer,
    votos_aprobado integer,
    votos_rechazado integer
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
-- Name: solicitudes_solicitudes_miembros_que_votaron; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE solicitudes_solicitudes_miembros_que_votaron (
    id integer NOT NULL,
    solicitudes_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.solicitudes_solicitudes_miembros_que_votaron OWNER TO sap;

--
-- Name: solicitudes_solicitudes_miembros_que_votaron_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE solicitudes_solicitudes_miembros_que_votaron_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.solicitudes_solicitudes_miembros_que_votaron_id_seq OWNER TO sap;

--
-- Name: solicitudes_solicitudes_miembros_que_votaron_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE solicitudes_solicitudes_miembros_que_votaron_id_seq OWNED BY solicitudes_solicitudes_miembros_que_votaron.id;


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
    id integer NOT NULL,
    user_id integer NOT NULL,
    telefono character varying(30) NOT NULL,
    direccion character varying(50) NOT NULL,
    especialidad character varying(50) NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public.usuarios_usuarios OWNER TO sap;

--
-- Name: usuarios_usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE usuarios_usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_usuarios_id_seq OWNER TO sap;

--
-- Name: usuarios_usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE usuarios_usuarios_id_seq OWNED BY usuarios_usuarios.id;


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

ALTER TABLE ONLY solicitudes_solicitudes ALTER COLUMN id SET DEFAULT nextval('solicitudes_solicitudes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes_miembros_que_votaron ALTER COLUMN id SET DEFAULT nextval('solicitudes_solicitudes_miembros_que_votaron_id_seq'::regclass);


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
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY usuarios_usuarios ALTER COLUMN id SET DEFAULT nextval('usuarios_usuarios_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_group (id, name) FROM stdin;
1	liderproyecto1
2	liderproyecto2
3	liderproyecto3
4	desarrollador1
5	desarrollador2
6	desarrollador3
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_id_seq', 6, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	40
2	1	37
3	1	39
4	1	41
5	1	38
6	1	35
7	1	36
8	1	30
9	1	32
10	1	34
11	1	33
12	1	31
13	1	26
14	1	29
15	1	27
16	1	23
17	1	28
18	1	25
19	1	24
20	1	45
21	1	42
22	1	44
23	1	46
24	1	43
25	1	22
26	1	19
27	1	21
28	1	20
29	1	75
30	1	77
31	1	76
32	1	81
33	1	83
34	1	82
35	1	78
36	1	80
37	1	79
38	1	90
39	1	93
40	1	87
41	1	89
42	1	92
43	1	91
44	1	88
45	1	84
46	1	86
47	1	85
48	1	94
49	1	96
50	1	95
51	1	67
52	1	66
53	1	74
54	1	71
55	1	68
56	1	70
57	1	72
58	1	73
59	1	69
60	2	40
61	2	37
62	2	39
63	2	41
64	2	38
65	2	35
66	2	36
67	2	30
68	2	32
69	2	34
70	2	33
71	2	31
72	2	26
73	2	29
74	2	27
75	2	23
76	2	28
77	2	25
78	2	24
79	2	45
80	2	42
81	2	44
82	2	46
83	2	43
84	2	22
85	2	19
86	2	21
87	2	20
88	2	75
89	2	77
90	2	76
91	2	81
92	2	83
93	2	82
94	2	78
95	2	80
96	2	79
97	2	90
98	2	93
99	2	87
100	2	89
101	2	92
102	2	91
103	2	88
104	2	84
105	2	86
106	2	85
107	2	94
108	2	96
109	2	95
110	2	67
111	2	66
112	2	74
113	2	71
114	2	68
115	2	70
116	2	72
117	2	73
118	2	69
119	3	40
120	3	37
121	3	39
122	3	41
123	3	38
124	3	35
125	3	36
126	3	30
127	3	32
128	3	34
129	3	33
130	3	31
131	3	26
132	3	29
133	3	27
134	3	23
135	3	28
136	3	25
137	3	24
138	3	45
139	3	42
140	3	44
141	3	46
142	3	43
143	3	22
144	3	19
145	3	21
146	3	20
147	3	75
148	3	77
149	3	76
150	3	81
151	3	83
152	3	82
153	3	78
154	3	80
155	3	79
156	3	90
157	3	93
158	3	87
159	3	89
160	3	92
161	3	91
162	3	88
163	3	84
164	3	86
165	3	85
166	3	94
167	3	96
168	3	95
169	3	67
170	3	66
171	3	74
172	3	71
173	3	68
174	3	70
175	3	72
176	3	73
177	3	69
178	4	40
179	4	37
180	4	39
181	4	41
182	4	38
183	4	35
184	4	36
185	4	30
186	4	32
187	4	34
188	4	33
189	4	31
190	4	26
191	4	29
192	4	27
193	4	23
194	4	28
195	4	25
196	4	24
197	4	45
198	4	42
199	4	44
200	4	46
201	4	43
202	4	22
203	4	19
204	4	21
205	4	20
206	4	75
207	4	77
208	4	76
209	4	81
210	4	83
211	4	82
212	4	78
213	4	80
214	4	79
215	4	90
216	4	93
217	4	87
218	4	89
219	4	92
220	4	91
221	4	88
222	4	84
223	4	86
224	4	85
225	4	94
226	4	96
227	4	95
228	4	67
229	4	66
230	4	74
231	4	71
232	4	68
233	4	70
234	4	72
235	4	73
236	4	69
237	5	40
238	5	37
239	5	39
240	5	41
241	5	38
242	5	35
243	5	36
244	5	30
245	5	32
246	5	34
247	5	33
248	5	31
249	5	26
250	5	29
251	5	27
252	5	23
253	5	28
254	5	25
255	5	24
256	5	45
257	5	42
258	5	44
259	5	46
260	5	43
261	5	22
262	5	19
263	5	21
264	5	20
265	5	75
266	5	77
267	5	76
268	5	81
269	5	83
270	5	82
271	5	78
272	5	80
273	5	79
274	5	90
275	5	93
276	5	87
277	5	89
278	5	92
279	5	91
280	5	88
281	5	84
282	5	86
283	5	85
284	5	94
285	5	96
286	5	95
287	5	67
288	5	66
289	5	74
290	5	71
291	5	68
292	5	70
293	5	72
294	5	73
295	5	69
296	6	40
297	6	37
298	6	39
299	6	41
300	6	38
301	6	35
302	6	36
303	6	30
304	6	32
305	6	34
306	6	33
307	6	31
308	6	26
309	6	29
310	6	27
311	6	23
312	6	28
313	6	25
314	6	24
315	6	45
316	6	42
317	6	44
318	6	46
319	6	43
320	6	22
321	6	19
322	6	21
323	6	20
324	6	75
325	6	77
326	6	76
327	6	81
328	6	83
329	6	82
330	6	78
331	6	80
332	6	79
333	6	90
334	6	93
335	6	87
336	6	89
337	6	92
338	6	91
339	6	88
340	6	84
341	6	86
342	6	85
343	6	94
344	6	96
345	6	95
346	6	67
347	6	66
348	6	74
349	6	71
350	6	68
351	6	70
352	6	72
353	6	73
354	6	69
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 354, true);


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
19	Puede crear usuarios	7	crear_usuarios
20	Puede modificar usuarios	7	modificar_usuarios
21	Puede eliminar usuarios	7	eliminar_usuarios
22	puede listar usuarios	7	administrar_usuario
23	Puede crear roles	8	crear_roles
24	Puede modificar roles	8	modificar_roles
25	Puede eliminar roles	8	eliminar_roles
26	puede listar los roles	8	administrar_roles
27	puede asignar un rol a un usuario	8	asignar_rol
28	puede desasignar un rol de un usuario	8	desasignar_rol
29	puede asignar un proyecto a un rol	8	asignar_proyecto_rol
30	Puede crear proyectos	9	crear_proyectos
31	Puede modificar proyectos	9	modificar_proyectos
32	Puede eliminar proyectos	9	eliminar_proyectos
33	Puede listar los miembros de un proyecto	9	listar_miembros
34	Puede importar proyectos	9	importar_proyectos
35	Puede consultar proyectos	9	consultar_proyectos
36	Puede consultar proyectos finalizados	9	consultar_proyectosfinalizados
37	Puede crear fases	10	crear_fases
38	Puede modificar fases	10	modificar_fases
39	Puede eliminar fases	10	eliminar_fases
40	puede listar las Fases	10	administrar_fases
41	puede importar fases	10	importar_fase
42	Puede crear tipo atributo	11	crear_tipoatributo
43	Puede modificar tipo atributo	11	modificar_tipoatributo
44	Puede eliminar tipo atributo	11	eliminar_tipoatributo
45	puede listar los tipos de atributo	11	administrar_tipos_de_atributo
46	puede importar un tipo de atributo	11	importar_tipo_de_atributo
47	Puede crear numerico	12	crear_numerico
48	Puede modificar numerico	12	modificar_numerico
49	Puede eliminar numerico	12	eliminar_numerico
50	Puede crear fecha	13	crear_fecha
51	Puede modificar fecha	13	modificar_fecha
52	Puede eliminar fecha	13	eliminar_fecha
53	Puede crear texto	14	crear_texto
54	Puede modificar texto	14	modificar_texto
55	Puede eliminar texto	14	eliminar_texto
56	Puede crear logico	15	crear_logico
57	Puede modificar logico	15	modificar_logico
58	Puede eliminar logico	15	eliminar_logico
59	Puede crear archivo externo	16	crear_archivoexterno
60	Puede modificar archivo externo	16	modificar_archivoexterno
61	Puede eliminar archivo externo	16	eliminar_archivoexterno
62	Puede crear imagen	17	crear_imagen
63	Puede modificar imagen	17	modificar_imagen
64	Puede eliminar imagen	17	eliminar_imagen
65	Puede crear lista atributo	18	crear_listaatributo
66	Puede modificar lista atributo	18	modificar_listaatributo
67	Puede eliminar lista atributo	18	eliminar_listaatributo
68	Puede crear tipo item	19	crear_tipoitem
69	Puede modificar tipo item	19	modificar_tipoitem
70	Puede eliminar tipo item	19	eliminar_tipoitem
71	Puede consultar los datos de un Tipo de Item	19	consultar_tipoitem
72	Puede gestionar un Tipo de Item	19	gestionar_tipoitem
73	Puede Importar un Tipo de Item	19	importar_tipoitem
74	Puede administrar los Tipos de Item	19	administrar_tipoitem
75	Puede crear items	20	crear_items
76	Puede modificar items	20	modificar_items
77	Puede eliminar items	20	eliminar_items
78	Puede crear valor item	21	crear_valoritem
79	Puede modificar valor item	21	modificar_valoritem
80	Puede eliminar valor item	21	eliminar_valoritem
81	Puede crear lista valores	22	crear_listavalores
82	Puede modificar lista valores	22	modificar_listavalores
83	Puede eliminar lista valores	22	eliminar_listavalores
84	Puede crear relaciones	23	crear_relaciones
85	Puede modificar relaciones	23	modificar_relaciones
86	Puede eliminar relaciones	23	eliminar_relaciones
87	Puede crear linea base	24	crear_lineabase
88	Puede modificar linea base	24	modificar_lineabase
89	Puede eliminar linea base	24	eliminar_lineabase
90	puede listar las Lineas Base	24	administrar_lineas_base
91	puede generar Linea Base	24	generar_linea_base
92	puede generar informe de Linea Base	24	generar_informe_linea_base
93	puede consultar datos de linea base Linea Base	24	consultar_linea_base
94	Puede crear solicitudes	25	crear_solicitudes
95	Puede modificar solicitudes	25	modificar_solicitudes
96	Puede eliminar solicitudes	25	eliminar_solicitudes
97	Puede crear comite	26	crear_comite
98	Puede modificar comite	26	modificar_comite
99	Puede eliminar comite	26	eliminar_comite
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_permission_id_seq', 99, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$12000$iAXvTU7Fjpp2$U5/zLGbhBxU7Cw23WrMSOkdD/nEGx4hNpi0ZddfKWAY=	2014-05-24 02:19:08.475991-04	f	ysapy	ysapy	ortiz	usuario1@sap	f	t	2014-05-24 02:19:08.475991-04
5	pbkdf2_sha256$12000$XZdbo3NkHNmZ$+LqjN1o3XR3k9GyOD+CPcP/fx3kVR35w/Fl6WxUfuAY=	2014-05-24 02:20:34.691677-04	f	usuario1	ysapy	ortiz	usuario1@sap	f	t	2014-05-24 02:20:34.691677-04
6	pbkdf2_sha256$12000$xIyA1nsfM9pr$SZgvyftmpdVmrYMDO47ZcFtWRbL1QYEKAN8DVuq4Mac=	2014-05-24 02:20:48.819724-04	f	usuario2	ysapy	ortiz	usuario1@sap	f	t	2014-05-24 02:20:48.819724-04
7	pbkdf2_sha256$12000$o48eLwB4kCkY$DlShC4Bra4VLxWLAq5fu3SPzdaVdMuJ9lkbhFAaKlyw=	2014-05-24 02:21:22.24037-04	f	usuario3	ysapy	ortiz	usuario1@sap	f	t	2014-05-24 02:21:22.24037-04
3	pbkdf2_sha256$12000$lxcwArRbnTIR$ukJ2pNrJomLH9L1EUVuPPbVlkp4zp4ya8xb9WVVBheA=	2014-05-24 02:31:48.609316-04	f	eduardo	ysapy	ortiz	ysapy@sap	f	t	2014-05-24 02:19:48.291595-04
1	pbkdf2_sha256$12000$1YKDtdIZAOe2$JJ4vCZ/NMpwF1EcTCtp7VD3rVo6LqyAPnUV9vZoprHk=	2014-05-24 02:34:02.089292-04	t	sap				t	t	2014-05-24 02:16:44.292721-04
4	pbkdf2_sha256$12000$blwHFnZP4HJ9$GUVw1Qczeu2gQO467ExnH4y6BUZLhUlOU640B1sRO9U=	2014-05-24 02:50:20.614863-04	f	marcelo	ysapy	ortiz	usuario1@sap	f	t	2014-05-24 02:20:09.047639-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
2	3	2
3	4	3
4	5	4
5	6	4
6	7	4
7	5	5
8	6	5
9	7	5
10	5	6
11	6	6
12	7	6
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 12, true);


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
1	2	6
2	2	7
3	2	3
4	3	5
5	3	6
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
7	usuarios	usuarios	usuarios
8	roles	roles	roles
9	proyectos	proyectos	proyectos
10	fases	fases	fases
11	tipo atributo	tipoatributo	tipoatributo
12	numerico	tipoatributo	numerico
13	fecha	tipoatributo	fecha
14	texto	tipoatributo	texto
15	logico	tipoatributo	logico
16	archivo externo	tipoatributo	archivoexterno
17	imagen	tipoatributo	imagen
18	lista atributo	tipoitem	listaatributo
19	tipo item	tipoitem	tipoitem
20	items	items	items
21	valor item	items	valoritem
22	lista valores	items	listavalores
23	relaciones	relaciones	relaciones
24	linea base	lineabase	lineabase
25	solicitudes	solicitudes	solicitudes
26	comite	comite	comite
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('django_content_type_id_seq', 26, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
fquuqplhipm1vv7vhcrj56uee3jgi4jd	NTMwOTM4YmIyYWZmM2VlMTZmOTE5MmJiYjZjOGU2YWRiODRiM2U4NDp7fQ==	2014-06-07 02:50:24.781991-04
\.


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY fases_fases (id, nombre, nombre_eliminado, descripcion, estado, fechainicio, duracion, proyecto_id, is_active, orden) FROM stdin;
1	Fase 1	\N	Fase 4 del proyecto 1	DF	2014-05-24	4	2	t	1
2	Fase 2	\N	Fase 4 del proyecto 1	DF	2014-05-24	4	2	t	2
3	Fase 1	\N	Fase 4 del proyecto 1	DR	2014-05-24	4	3	t	1
4	Fase 2	\N	Fase 4 del proyecto 1	DR	2014-05-24	4	3	t	2
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('fases_fases_id_seq', 4, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_items (id, nombre, version, prioridad, estado, descripcion, observaciones, "costoMonetario", "costoTemporal", complejidad, fase_id, proyecto_id, is_active, tipo_item_id, padre, lb) FROM stdin;
2	item2fase1	1	1	Bloqueado	Fase 1 del proyecto 1	ninguna	43434	45	1	3	3	t	1	0	\N
1	item1fase1	1	1	Bloqueado	Fase 4 del proyecto 1	ninguna	8	45	1	3	3	t	1	0	\N
3	item1fase2	1	1	En Construccion	Fase 4 del proyecto 1	ninguna	43434	45	1	4	3	t	1	0	\N
4	item2fase2	2	1	Terminado	Fase 4 del proyecto 1	ninguna	43434	3	1	4	3	t	1	2	\N
\.


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_items_id_seq', 4, true);


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
1	1	3	3	t		2014-05-24
\.


--
-- Name: lineabase_lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_id_seq', 1, true);


--
-- Data for Name: lineabase_lineabase_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY lineabase_lineabase_items (id, lineabase_id, items_id) FROM stdin;
1	1	2
2	1	1
\.


--
-- Name: lineabase_lineabase_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_items_id_seq', 2, true);


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY proyectos_proyectos (id, nombre, lider_id, estado, fecha_inicio, duracion, is_active) FROM stdin;
1	Proyecto 1	2	Inactivo	2014-04-04	4	t
2	Proyecto 2	3	En Construccion	2014-04-04	4	t
3	Proyecto 3	4	En Construccion	2014-04-04	3	t
\.


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 3, true);


--
-- Data for Name: relaciones_relaciones; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY relaciones_relaciones (id, nombre, padre_id, item, version) FROM stdin;
1	\N	2	4	2
\.


--
-- Name: relaciones_relaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('relaciones_relaciones_id_seq', 1, true);


--
-- Data for Name: roles_roles; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY roles_roles (group_ptr_id, proyecto, descripcion, is_active) FROM stdin;
1	1		t
2	2		t
3	3		t
4	1		t
5	2		t
6	3		t
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
-- Data for Name: solicitudes_solicitudes; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_solicitudes (id, nombre, usuario_id, proyecto_id, fase_id, item_id, fecha_solicitud, tiempo_solicitado, descripcion, observaciones, estado, tiempo_esperado, votos_aprobado, votos_rechazado) FROM stdin;
1	\N	4	3	3	2	2014-05-24	4	se necesita cargar atributos	ninguna	Pendiente	2	1	0
\.


--
-- Name: solicitudes_solicitudes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_solicitudes_id_seq', 1, true);


--
-- Data for Name: solicitudes_solicitudes_miembros_que_votaron; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY solicitudes_solicitudes_miembros_que_votaron (id, solicitudes_id, user_id) FROM stdin;
1	1	4
\.


--
-- Name: solicitudes_solicitudes_miembros_que_votaron_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('solicitudes_solicitudes_miembros_que_votaron_id_seq', 1, true);


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
2	nombre	Texto	0	10	f		t
3	fecha	Fecha	0	0	f		t
\.


--
-- Name: tipoatributo_tipoatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_id_seq', 3, true);


--
-- Data for Name: tipoatributo_tipoatributo_proyecto; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_tipoatributo_proyecto (id, tipoatributo_id, proyectos_id) FROM stdin;
1	1	3
2	2	3
3	3	3
\.


--
-- Name: tipoatributo_tipoatributo_proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_proyecto_id_seq', 3, true);


--
-- Data for Name: tipoitem_listaatributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_listaatributo (id, id_atributo, id_tipoitem, orden, nombre, is_active) FROM stdin;
1	1	1	1	cantidad	t
2	3	1	2	fecha	t
3	2	1	3	nombre	t
\.


--
-- Name: tipoitem_listaatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_listaatributo_id_seq', 3, true);


--
-- Data for Name: tipoitem_tipoitem; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_tipoitem (id, nombre, descripcion, id_proyecto, is_active) FROM stdin;
1	requerimiento	requerimientos	3	t
\.


--
-- Name: tipoitem_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_tipoitem_id_seq', 1, true);


--
-- Data for Name: tipoitem_tipoitem_listaAtributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY "tipoitem_tipoitem_listaAtributo" (id, tipoitem_id, listaatributo_id) FROM stdin;
1	1	1
2	1	2
3	1	3
\.


--
-- Name: tipoitem_tipoitem_listaAtributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('"tipoitem_tipoitem_listaAtributo_id_seq"', 3, true);


--
-- Data for Name: usuarios_usuarios; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY usuarios_usuarios (id, user_id, telefono, direccion, especialidad, observaciones) FROM stdin;
1	1				
2	2	021	lambare	desarrollador	ninguna
3	3	021	lambare	desarrollador	ninguna
4	4	021	lambare	desarrollador	ninguna
5	5	021	lambare	desarrollador	ninguna
6	6	021	lambare	desarrollador	ninguna
7	7	021	lambare	desarrollador	ninguna
\.


--
-- Name: usuarios_usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('usuarios_usuarios_id_seq', 7, true);


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
-- Name: solicitudes_solicitudes_miembros_que_solicitudes_id_user_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY solicitudes_solicitudes_miembros_que_votaron
    ADD CONSTRAINT solicitudes_solicitudes_miembros_que_solicitudes_id_user_id_key UNIQUE (solicitudes_id, user_id);


--
-- Name: solicitudes_solicitudes_miembros_que_votaron_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY solicitudes_solicitudes_miembros_que_votaron
    ADD CONSTRAINT solicitudes_solicitudes_miembros_que_votaron_pkey PRIMARY KEY (id);


--
-- Name: solicitudes_solicitudes_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_pkey PRIMARY KEY (id);


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
    ADD CONSTRAINT usuarios_usuarios_pkey PRIMARY KEY (id);


--
-- Name: usuarios_usuarios_user_id_key; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY usuarios_usuarios
    ADD CONSTRAINT usuarios_usuarios_user_id_key UNIQUE (user_id);


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
-- Name: solicitudes_solicitudes_fase_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_fase_id ON solicitudes_solicitudes USING btree (fase_id);


--
-- Name: solicitudes_solicitudes_item_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_item_id ON solicitudes_solicitudes USING btree (item_id);


--
-- Name: solicitudes_solicitudes_miembros_que_votaron_solicitudes_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_miembros_que_votaron_solicitudes_id ON solicitudes_solicitudes_miembros_que_votaron USING btree (solicitudes_id);


--
-- Name: solicitudes_solicitudes_miembros_que_votaron_user_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_miembros_que_votaron_user_id ON solicitudes_solicitudes_miembros_que_votaron USING btree (user_id);


--
-- Name: solicitudes_solicitudes_proyecto_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_proyecto_id ON solicitudes_solicitudes USING btree (proyecto_id);


--
-- Name: solicitudes_solicitudes_usuario_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX solicitudes_solicitudes_usuario_id ON solicitudes_solicitudes USING btree (usuario_id);


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
    ADD CONSTRAINT comite_comite_miembros_usuarios_id_fkey FOREIGN KEY (usuarios_id) REFERENCES usuarios_usuarios(id) DEFERRABLE INITIALLY DEFERRED;


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
-- Name: solicitudes_id_refs_id_e2c6bdc7; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes_miembros_que_votaron
    ADD CONSTRAINT solicitudes_id_refs_id_e2c6bdc7 FOREIGN KEY (solicitudes_id) REFERENCES solicitudes_solicitudes(id) DEFERRABLE INITIALLY DEFERRED;


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
-- Name: solicitudes_solicitudes_miembros_que_votaron_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes_miembros_que_votaron
    ADD CONSTRAINT solicitudes_solicitudes_miembros_que_votaron_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_solicitudes_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: solicitudes_solicitudes_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY solicitudes_solicitudes
    ADD CONSTRAINT solicitudes_solicitudes_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuarios_usuarios(id) DEFERRABLE INITIALLY DEFERRED;


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

