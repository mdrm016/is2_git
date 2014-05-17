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
ALTER TABLE ONLY public.roles_roles DROP CONSTRAINT roles_roles_group_ptr_id_fkey;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT roles_id_refs_group_ptr_id_11e17ff0;
ALTER TABLE ONLY public.relaciones_versionrelacion DROP CONSTRAINT relaciones_versionrelacion_relacion_id_fkey;
ALTER TABLE ONLY public.relaciones_versionrelacion DROP CONSTRAINT relaciones_versionrelacion_item_id_fkey;
ALTER TABLE ONLY public.proyectos_proyectos DROP CONSTRAINT proyectos_proyectos_lider_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase DROP CONSTRAINT lineabase_lineabase_proyecto_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase_items DROP CONSTRAINT lineabase_lineabase_items_items_id_fkey;
ALTER TABLE ONLY public.lineabase_lineabase DROP CONSTRAINT lineabase_lineabase_fase_id_fkey;
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
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_permission_id_fkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fkey;
DROP INDEX public."tipoitem_tipoitem_listaAtributo_tipoitem_id";
DROP INDEX public."tipoitem_tipoitem_listaAtributo_listaatributo_id";
DROP INDEX public.tipoatributo_tipoatributo_proyecto_tipoatributo_id;
DROP INDEX public.tipoatributo_tipoatributo_proyecto_proyectos_id;
DROP INDEX public.tipoatributo_tipoatributo_nombre_like;
DROP INDEX public.roles_roles_fases_roles_id;
DROP INDEX public.roles_roles_fases_fases_id;
DROP INDEX public.relaciones_versionrelacion_relacion_id;
DROP INDEX public.relaciones_versionrelacion_item_id;
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
ALTER TABLE ONLY public.roles_roles DROP CONSTRAINT roles_roles_pkey;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT roles_roles_fases_roles_id_fases_id_key;
ALTER TABLE ONLY public.roles_roles_fases DROP CONSTRAINT roles_roles_fases_pkey;
ALTER TABLE ONLY public.relaciones_versionrelacion DROP CONSTRAINT relaciones_versionrelacion_pkey;
ALTER TABLE ONLY public.relaciones_relaciones DROP CONSTRAINT relaciones_relaciones_pkey;
ALTER TABLE ONLY public.relaciones_listarelacion DROP CONSTRAINT relaciones_listarelacion_pkey;
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
ALTER TABLE public.roles_roles_fases ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.relaciones_versionrelacion ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.relaciones_relaciones ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.relaciones_listarelacion ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.proyectos_proyectos ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.lineabase_lineabase_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.lineabase_lineabase ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_valoritem ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_listavalores ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.items_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.fases_fases ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
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
DROP SEQUENCE public.roles_roles_fases_id_seq;
DROP TABLE public.roles_roles_fases;
DROP TABLE public.roles_roles;
DROP SEQUENCE public.relaciones_versionrelacion_id_seq;
DROP TABLE public.relaciones_versionrelacion;
DROP SEQUENCE public.relaciones_relaciones_id_seq;
DROP TABLE public.relaciones_relaciones;
DROP SEQUENCE public.relaciones_listarelacion_id_seq;
DROP TABLE public.relaciones_listarelacion;
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
    padre integer
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
-- Name: relaciones_listarelacion; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE relaciones_listarelacion (
    id integer NOT NULL,
    nombre character varying(30),
    nombreitem character varying(30),
    relacion integer
);


ALTER TABLE public.relaciones_listarelacion OWNER TO sap;

--
-- Name: relaciones_listarelacion_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE relaciones_listarelacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relaciones_listarelacion_id_seq OWNER TO sap;

--
-- Name: relaciones_listarelacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE relaciones_listarelacion_id_seq OWNED BY relaciones_listarelacion.id;


--
-- Name: relaciones_relaciones; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE relaciones_relaciones (
    id integer NOT NULL,
    nombre character varying(30),
    padre integer,
    antecesor integer,
    sucesor integer,
    hijo integer
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
-- Name: relaciones_versionrelacion; Type: TABLE; Schema: public; Owner: sap; Tablespace: 
--

CREATE TABLE relaciones_versionrelacion (
    id integer NOT NULL,
    nombre character varying(30),
    relacion_id integer NOT NULL,
    item_id integer NOT NULL,
    version integer
);


ALTER TABLE public.relaciones_versionrelacion OWNER TO sap;

--
-- Name: relaciones_versionrelacion_id_seq; Type: SEQUENCE; Schema: public; Owner: sap
--

CREATE SEQUENCE relaciones_versionrelacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relaciones_versionrelacion_id_seq OWNER TO sap;

--
-- Name: relaciones_versionrelacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sap
--

ALTER SEQUENCE relaciones_versionrelacion_id_seq OWNED BY relaciones_versionrelacion.id;


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

ALTER TABLE ONLY relaciones_listarelacion ALTER COLUMN id SET DEFAULT nextval('relaciones_listarelacion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY relaciones_relaciones ALTER COLUMN id SET DEFAULT nextval('relaciones_relaciones_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY relaciones_versionrelacion ALTER COLUMN id SET DEFAULT nextval('relaciones_versionrelacion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: sap
--

ALTER TABLE ONLY roles_roles_fases ALTER COLUMN id SET DEFAULT nextval('roles_roles_fases_id_seq'::regclass);


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
1	Jefe Supremo
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, true);


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
38	1	96
39	1	93
40	1	95
41	1	98
42	1	97
43	1	94
44	1	90
45	1	92
46	1	91
47	1	84
48	1	86
49	1	85
50	1	87
51	1	89
52	1	88
53	1	67
54	1	66
55	1	74
56	1	71
57	1	68
58	1	70
59	1	72
60	1	73
61	1	69
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 61, true);


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
87	Puede crear version relacion	24	crear_versionrelacion
88	Puede modificar version relacion	24	modificar_versionrelacion
89	Puede eliminar version relacion	24	eliminar_versionrelacion
90	Puede crear lista relacion	25	crear_listarelacion
91	Puede modificar lista relacion	25	modificar_listarelacion
92	Puede eliminar lista relacion	25	eliminar_listarelacion
93	Puede crear linea base	26	crear_lineabase
94	Puede modificar linea base	26	modificar_lineabase
95	Puede eliminar linea base	26	eliminar_lineabase
96	puede listar las Lineas Base	26	administrar_lineas_base
97	puede generar Linea Base	26	generar_linea_base
98	puede generar informe de Linea Base	26	generar_informe_linea_base
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_permission_id_seq', 98, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$12000$SYT45RfuId8F$shIhqAVg9jA0PjMUREr6GTrF6t8aCz15tfalu/n++pM=	2014-05-11 10:32:47.660185-04	t	sap				t	t	2014-05-10 13:44:19.754374-04
2	pbkdf2_sha256$12000$aqkkrIpvtJs1$t1Jcu6191gigcyDt2jM6MJrIMv9u606XazELtSlJ4Y8=	2014-05-11 10:33:45.06293-04	f	edugimenez	Eduardo	Gimenez	eduardogimenez8@gmail.com	f	t	2014-05-11 10:23:55.529282-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('auth_user_id_seq', 2, true);


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
24	version relacion	relaciones	versionrelacion
25	lista relacion	relaciones	listarelacion
26	linea base	lineabase	lineabase
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('django_content_type_id_seq', 26, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
1lp4var4al06dipydq7t9pu4i8n26eif	ZTVhODExMDk3MDI5MTRiNmNmZGYzOWUyNWYxZTFmM2I4NzljODZlNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-05-25 10:33:45.088101-04
\.


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY fases_fases (id, nombre, nombre_eliminado, descripcion, estado, fechainicio, duracion, proyecto_id, is_active, orden) FROM stdin;
1	hhhhh	\N	gcvg	DR	2014-05-11	1	1	t	1
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('fases_fases_id_seq', 1, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY items_items (id, nombre, version, prioridad, estado, descripcion, observaciones, "costoMonetario", "costoTemporal", complejidad, fase_id, proyecto_id, is_active, tipo_item_id, padre) FROM stdin;
2	Analisis	1	9	Bloqueado	ksnbsn	kajjnkjv	9	7	2	1	1	t	1	0
3	Construccion	1	4	Validado	skdnsj	sdgdsrg	5	4	2	1	1	t	1	0
1	Requerimientos	1	7	Bloqueado	jbkjbj	jkbkjb	9	9	6	1	1	t	1	0
\.


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('items_items_id_seq', 3, true);


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
1	1	1	1	t		2014-05-13
2	2	1	1	t	ebdsbdsb	2014-05-13
\.


--
-- Name: lineabase_lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_id_seq', 2, true);


--
-- Data for Name: lineabase_lineabase_items; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY lineabase_lineabase_items (id, lineabase_id, items_id) FROM stdin;
5	1	2
6	2	1
\.


--
-- Name: lineabase_lineabase_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('lineabase_lineabase_items_id_seq', 6, true);


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY proyectos_proyectos (id, nombre, lider_id, estado, fecha_inicio, duracion, is_active) FROM stdin;
1	Andromeda	2	En Construccion	2014-05-21	5	t
\.


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 1, true);


--
-- Data for Name: relaciones_listarelacion; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY relaciones_listarelacion (id, nombre, nombreitem, relacion) FROM stdin;
\.


--
-- Name: relaciones_listarelacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('relaciones_listarelacion_id_seq', 1, false);


--
-- Data for Name: relaciones_relaciones; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY relaciones_relaciones (id, nombre, padre, antecesor, sucesor, hijo) FROM stdin;
\.


--
-- Name: relaciones_relaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('relaciones_relaciones_id_seq', 1, false);


--
-- Data for Name: relaciones_versionrelacion; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY relaciones_versionrelacion (id, nombre, relacion_id, item_id, version) FROM stdin;
\.


--
-- Name: relaciones_versionrelacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('relaciones_versionrelacion_id_seq', 1, false);


--
-- Data for Name: roles_roles; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY roles_roles (group_ptr_id, proyecto, descripcion, is_active) FROM stdin;
1	1	Usuario aleatorio que posee todos los permisos	t
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
1	Edad	Numerico	0	2	t		t
\.


--
-- Name: tipoatributo_tipoatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_id_seq', 1, true);


--
-- Data for Name: tipoatributo_tipoatributo_proyecto; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoatributo_tipoatributo_proyecto (id, tipoatributo_id, proyectos_id) FROM stdin;
1	1	1
\.


--
-- Name: tipoatributo_tipoatributo_proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoatributo_tipoatributo_proyecto_id_seq', 1, true);


--
-- Data for Name: tipoitem_listaatributo; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_listaatributo (id, id_atributo, id_tipoitem, orden, nombre, is_active) FROM stdin;
1	1	1	1	Edad	t
\.


--
-- Name: tipoitem_listaatributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('tipoitem_listaatributo_id_seq', 1, true);


--
-- Data for Name: tipoitem_tipoitem; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY tipoitem_tipoitem (id, nombre, descripcion, id_proyecto, is_active) FROM stdin;
1	Ficha	hghgchgc	1	t
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
\.


--
-- Name: tipoitem_tipoitem_listaAtributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('"tipoitem_tipoitem_listaAtributo_id_seq"', 1, true);


--
-- Data for Name: usuarios_usuarios; Type: TABLE DATA; Schema: public; Owner: sap
--

COPY usuarios_usuarios (id, user_id, telefono, direccion, especialidad, observaciones) FROM stdin;
1	1				
2	2	999000	sdjvbskjb s	Analista	MMMMM
\.


--
-- Name: usuarios_usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sap
--

SELECT pg_catalog.setval('usuarios_usuarios_id_seq', 2, true);


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
-- Name: relaciones_listarelacion_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY relaciones_listarelacion
    ADD CONSTRAINT relaciones_listarelacion_pkey PRIMARY KEY (id);


--
-- Name: relaciones_relaciones_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY relaciones_relaciones
    ADD CONSTRAINT relaciones_relaciones_pkey PRIMARY KEY (id);


--
-- Name: relaciones_versionrelacion_pkey; Type: CONSTRAINT; Schema: public; Owner: sap; Tablespace: 
--

ALTER TABLE ONLY relaciones_versionrelacion
    ADD CONSTRAINT relaciones_versionrelacion_pkey PRIMARY KEY (id);


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
-- Name: relaciones_versionrelacion_item_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX relaciones_versionrelacion_item_id ON relaciones_versionrelacion USING btree (item_id);


--
-- Name: relaciones_versionrelacion_relacion_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX relaciones_versionrelacion_relacion_id ON relaciones_versionrelacion USING btree (relacion_id);


--
-- Name: roles_roles_fases_fases_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX roles_roles_fases_fases_id ON roles_roles_fases USING btree (fases_id);


--
-- Name: roles_roles_fases_roles_id; Type: INDEX; Schema: public; Owner: sap; Tablespace: 
--

CREATE INDEX roles_roles_fases_roles_id ON roles_roles_fases USING btree (roles_id);


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
-- Name: relaciones_versionrelacion_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY relaciones_versionrelacion
    ADD CONSTRAINT relaciones_versionrelacion_item_id_fkey FOREIGN KEY (item_id) REFERENCES items_items(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: relaciones_versionrelacion_relacion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: sap
--

ALTER TABLE ONLY relaciones_versionrelacion
    ADD CONSTRAINT relaciones_versionrelacion_relacion_id_fkey FOREIGN KEY (relacion_id) REFERENCES relaciones_relaciones(id) DEFERRABLE INITIALLY DEFERRED;


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

