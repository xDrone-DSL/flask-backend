// Generated from C:/Users/jxzk1/Desktop/xdrone-dsl/flask-backend/antlr\xDroneLexer.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class xDroneLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MAIN=1, TAKEOFF=2, LAND=3, UP=4, DOWN=5, LEFT=6, RIGHT=7, FORWARD=8, BACKWARD=9, 
		ROTATE_LEFT=10, ROTATE_RIGHT=11, WAIT=12, AT=13, INSERT=14, REMOVE=15, 
		SIZE=16, IF=17, ELSE=18, WHILE=19, FOR=20, FROM=21, TO=22, REPEAT=23, 
		TIMES=24, FUNCTION=25, RETURN=26, TYPE_INT=27, TYPE_DECIMAL=28, TYPE_STRING=29, 
		TYPE_BOOLEAN=30, TYPE_VECTOR=31, TYPE_LIST=32, TRUE=33, FALSE=34, VEC_X=35, 
		VEC_Y=36, VEC_Z=37, MULTI=38, DIV=39, PLUS=40, MINUS=41, CONCAT=42, GREATER=43, 
		GREATER_EQ=44, LESS=45, LESS_EQ=46, EQ=47, NOT_EQ=48, NOT=49, AND=50, 
		OR=51, L_PAR=52, R_PAR=53, L_BRACKET=54, R_BRACKET=55, L_BRACE=56, R_BRACE=57, 
		DOT=58, COMMA=59, SEMICOLON=60, ARROW=61, COMMENT=62, WS=63, IDENT=64, 
		SIGNED_INT=65, SIGNED_FLOAT=66, ESCAPED_STRING=67;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MAIN", "TAKEOFF", "LAND", "UP", "DOWN", "LEFT", "RIGHT", "FORWARD", 
			"BACKWARD", "ROTATE_LEFT", "ROTATE_RIGHT", "WAIT", "AT", "INSERT", "REMOVE", 
			"SIZE", "IF", "ELSE", "WHILE", "FOR", "FROM", "TO", "REPEAT", "TIMES", 
			"FUNCTION", "RETURN", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", 
			"TYPE_VECTOR", "TYPE_LIST", "TRUE", "FALSE", "VEC_X", "VEC_Y", "VEC_Z", 
			"MULTI", "DIV", "PLUS", "MINUS", "CONCAT", "GREATER", "GREATER_EQ", "LESS", 
			"LESS_EQ", "EQ", "NOT_EQ", "NOT", "AND", "OR", "L_PAR", "R_PAR", "L_BRACKET", 
			"R_BRACKET", "L_BRACE", "R_BRACE", "DOT", "COMMA", "SEMICOLON", "ARROW", 
			"DIGIT", "LOWERCASE", "UPPERCASE", "UNDERSCORE", "COMMENT", "WS", "IDENT", 
			"INT", "SIGNED_INT", "DECIMAL", "EXP", "FLOAT", "SIGNED_FLOAT", "DOUBLE_QUOTE", 
			"ESCAPED_CHAR", "CHARACTER", "ESCAPED_STRING"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'main'", "'takeoff'", "'land'", "'up'", "'down'", "'left'", "'right'", 
			"'forward'", "'backward'", "'rotate_left'", "'rotate_right'", "'wait'", 
			"'at'", "'insert'", "'remove'", "'size'", "'if'", "'else'", "'while'", 
			"'for'", "'from'", "'to'", "'repeat'", "'times'", "'function'", "'return'", 
			"'int'", "'decimal'", "'string'", "'boolean'", "'vector'", "'list'", 
			"'true'", "'false'", "'x'", "'y'", "'z'", "'*'", "'/'", "'+'", "'-'", 
			"'&'", "'>'", "'>='", "'<'", "'<='", "'=='", "'=/='", "'not'", "'and'", 
			"'or'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", 
			"'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MAIN", "TAKEOFF", "LAND", "UP", "DOWN", "LEFT", "RIGHT", "FORWARD", 
			"BACKWARD", "ROTATE_LEFT", "ROTATE_RIGHT", "WAIT", "AT", "INSERT", "REMOVE", 
			"SIZE", "IF", "ELSE", "WHILE", "FOR", "FROM", "TO", "REPEAT", "TIMES", 
			"FUNCTION", "RETURN", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", 
			"TYPE_VECTOR", "TYPE_LIST", "TRUE", "FALSE", "VEC_X", "VEC_Y", "VEC_Z", 
			"MULTI", "DIV", "PLUS", "MINUS", "CONCAT", "GREATER", "GREATER_EQ", "LESS", 
			"LESS_EQ", "EQ", "NOT_EQ", "NOT", "AND", "OR", "L_PAR", "R_PAR", "L_BRACKET", 
			"R_BRACKET", "L_BRACE", "R_BRACE", "DOT", "COMMA", "SEMICOLON", "ARROW", 
			"COMMENT", "WS", "IDENT", "SIGNED_INT", "SIGNED_FLOAT", "ESCAPED_STRING"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public xDroneLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "xDroneLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E\u0220\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6"+
		"\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3"+
		"\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3"+
		"\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3"+
		"\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3"+
		"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3"+
		"\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3"+
		"\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3"+
		" \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#"+
		"\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3"+
		".\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3"+
		"\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38"+
		"\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C"+
		"\7C\u01be\nC\fC\16C\u01c1\13C\3C\3C\3C\3C\3D\6D\u01c8\nD\rD\16D\u01c9"+
		"\3D\3D\3E\3E\3E\5E\u01d1\nE\3E\3E\3E\3E\7E\u01d7\nE\fE\16E\u01da\13E\3"+
		"F\6F\u01dd\nF\rF\16F\u01de\3G\5G\u01e2\nG\3G\3G\3H\3H\3H\5H\u01e9\nH\3"+
		"H\3H\5H\u01ed\nH\3I\3I\3I\3J\3J\3J\3J\3J\5J\u01f7\nJ\5J\u01f9\nJ\3K\5"+
		"K\u01fc\nK\3K\3K\3L\3L\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3"+
		"M\5M\u0212\nM\3N\3N\5N\u0216\nN\3O\3O\7O\u021a\nO\fO\16O\u021d\13O\3O"+
		"\3O\2\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17"+
		"\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35"+
		"9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66"+
		"k\67m8o9q:s;u<w=y>{?}\2\177\2\u0081\2\u0083\2\u0085@\u0087A\u0089B\u008b"+
		"\2\u008dC\u008f\2\u0091\2\u0093\2\u0095D\u0097\2\u0099\2\u009b\2\u009d"+
		"E\3\2\n\3\2\62;\3\2c|\3\2C\\\4\2\f\f\17\17\5\2\13\f\17\17\"\"\4\2--//"+
		"\4\2GGgg\5\2$$))^^\2\u022c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3"+
		"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2"+
		"\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67"+
		"\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2"+
		"\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2"+
		"\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]"+
		"\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2"+
		"\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2"+
		"\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089"+
		"\3\2\2\2\2\u008d\3\2\2\2\2\u0095\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2"+
		"\2\5\u00a4\3\2\2\2\7\u00ac\3\2\2\2\t\u00b1\3\2\2\2\13\u00b4\3\2\2\2\r"+
		"\u00b9\3\2\2\2\17\u00be\3\2\2\2\21\u00c4\3\2\2\2\23\u00cc\3\2\2\2\25\u00d5"+
		"\3\2\2\2\27\u00e1\3\2\2\2\31\u00ee\3\2\2\2\33\u00f3\3\2\2\2\35\u00f6\3"+
		"\2\2\2\37\u00fd\3\2\2\2!\u0104\3\2\2\2#\u0109\3\2\2\2%\u010c\3\2\2\2\'"+
		"\u0111\3\2\2\2)\u0117\3\2\2\2+\u011b\3\2\2\2-\u0120\3\2\2\2/\u0123\3\2"+
		"\2\2\61\u012a\3\2\2\2\63\u0130\3\2\2\2\65\u0139\3\2\2\2\67\u0140\3\2\2"+
		"\29\u0144\3\2\2\2;\u014c\3\2\2\2=\u0153\3\2\2\2?\u015b\3\2\2\2A\u0162"+
		"\3\2\2\2C\u0167\3\2\2\2E\u016c\3\2\2\2G\u0172\3\2\2\2I\u0174\3\2\2\2K"+
		"\u0176\3\2\2\2M\u0178\3\2\2\2O\u017a\3\2\2\2Q\u017c\3\2\2\2S\u017e\3\2"+
		"\2\2U\u0180\3\2\2\2W\u0182\3\2\2\2Y\u0184\3\2\2\2[\u0187\3\2\2\2]\u0189"+
		"\3\2\2\2_\u018c\3\2\2\2a\u018f\3\2\2\2c\u0193\3\2\2\2e\u0197\3\2\2\2g"+
		"\u019b\3\2\2\2i\u019e\3\2\2\2k\u01a0\3\2\2\2m\u01a2\3\2\2\2o\u01a4\3\2"+
		"\2\2q\u01a6\3\2\2\2s\u01a8\3\2\2\2u\u01aa\3\2\2\2w\u01ac\3\2\2\2y\u01ae"+
		"\3\2\2\2{\u01b0\3\2\2\2}\u01b3\3\2\2\2\177\u01b5\3\2\2\2\u0081\u01b7\3"+
		"\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01bb\3\2\2\2\u0087\u01c7\3\2\2\2\u0089"+
		"\u01d0\3\2\2\2\u008b\u01dc\3\2\2\2\u008d\u01e1\3\2\2\2\u008f\u01ec\3\2"+
		"\2\2\u0091\u01ee\3\2\2\2\u0093\u01f8\3\2\2\2\u0095\u01fb\3\2\2\2\u0097"+
		"\u01ff\3\2\2\2\u0099\u0211\3\2\2\2\u009b\u0215\3\2\2\2\u009d\u0217\3\2"+
		"\2\2\u009f\u00a0\7o\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3"+
		"\7p\2\2\u00a3\4\3\2\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7"+
		"\7m\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7h\2\2\u00aa"+
		"\u00ab\7h\2\2\u00ab\6\3\2\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7c\2\2\u00ae"+
		"\u00af\7p\2\2\u00af\u00b0\7f\2\2\u00b0\b\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2"+
		"\u00b3\7r\2\2\u00b3\n\3\2\2\2\u00b4\u00b5\7f\2\2\u00b5\u00b6\7q\2\2\u00b6"+
		"\u00b7\7y\2\2\u00b7\u00b8\7p\2\2\u00b8\f\3\2\2\2\u00b9\u00ba\7n\2\2\u00ba"+
		"\u00bb\7g\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd\7v\2\2\u00bd\16\3\2\2\2\u00be"+
		"\u00bf\7t\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7i\2\2\u00c1\u00c2\7j\2\2"+
		"\u00c2\u00c3\7v\2\2\u00c3\20\3\2\2\2\u00c4\u00c5\7h\2\2\u00c5\u00c6\7"+
		"q\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7y\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca"+
		"\7t\2\2\u00ca\u00cb\7f\2\2\u00cb\22\3\2\2\2\u00cc\u00cd\7d\2\2\u00cd\u00ce"+
		"\7c\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0\7m\2\2\u00d0\u00d1\7y\2\2\u00d1"+
		"\u00d2\7c\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7f\2\2\u00d4\24\3\2\2\2\u00d5"+
		"\u00d6\7t\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7c\2\2"+
		"\u00d9\u00da\7v\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7a\2\2\u00dc\u00dd"+
		"\7n\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7h\2\2\u00df\u00e0\7v\2\2\u00e0"+
		"\26\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7v\2\2\u00e4"+
		"\u00e5\7c\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7a\2\2"+
		"\u00e8\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7i\2\2\u00eb\u00ec"+
		"\7j\2\2\u00ec\u00ed\7v\2\2\u00ed\30\3\2\2\2\u00ee\u00ef\7y\2\2\u00ef\u00f0"+
		"\7c\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7v\2\2\u00f2\32\3\2\2\2\u00f3\u00f4"+
		"\7c\2\2\u00f4\u00f5\7v\2\2\u00f5\34\3\2\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8"+
		"\7p\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7t\2\2\u00fb"+
		"\u00fc\7v\2\2\u00fc\36\3\2\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff"+
		"\u0100\7o\2\2\u0100\u0101\7q\2\2\u0101\u0102\7x\2\2\u0102\u0103\7g\2\2"+
		"\u0103 \3\2\2\2\u0104\u0105\7u\2\2\u0105\u0106\7k\2\2\u0106\u0107\7|\2"+
		"\2\u0107\u0108\7g\2\2\u0108\"\3\2\2\2\u0109\u010a\7k\2\2\u010a\u010b\7"+
		"h\2\2\u010b$\3\2\2\2\u010c\u010d\7g\2\2\u010d\u010e\7n\2\2\u010e\u010f"+
		"\7u\2\2\u010f\u0110\7g\2\2\u0110&\3\2\2\2\u0111\u0112\7y\2\2\u0112\u0113"+
		"\7j\2\2\u0113\u0114\7k\2\2\u0114\u0115\7n\2\2\u0115\u0116\7g\2\2\u0116"+
		"(\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119\7q\2\2\u0119\u011a\7t\2\2\u011a"+
		"*\3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d\7t\2\2\u011d\u011e\7q\2\2\u011e"+
		"\u011f\7o\2\2\u011f,\3\2\2\2\u0120\u0121\7v\2\2\u0121\u0122\7q\2\2\u0122"+
		".\3\2\2\2\u0123\u0124\7t\2\2\u0124\u0125\7g\2\2\u0125\u0126\7r\2\2\u0126"+
		"\u0127\7g\2\2\u0127\u0128\7c\2\2\u0128\u0129\7v\2\2\u0129\60\3\2\2\2\u012a"+
		"\u012b\7v\2\2\u012b\u012c\7k\2\2\u012c\u012d\7o\2\2\u012d\u012e\7g\2\2"+
		"\u012e\u012f\7u\2\2\u012f\62\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132\7"+
		"w\2\2\u0132\u0133\7p\2\2\u0133\u0134\7e\2\2\u0134\u0135\7v\2\2\u0135\u0136"+
		"\7k\2\2\u0136\u0137\7q\2\2\u0137\u0138\7p\2\2\u0138\64\3\2\2\2\u0139\u013a"+
		"\7t\2\2\u013a\u013b\7g\2\2\u013b\u013c\7v\2\2\u013c\u013d\7w\2\2\u013d"+
		"\u013e\7t\2\2\u013e\u013f\7p\2\2\u013f\66\3\2\2\2\u0140\u0141\7k\2\2\u0141"+
		"\u0142\7p\2\2\u0142\u0143\7v\2\2\u01438\3\2\2\2\u0144\u0145\7f\2\2\u0145"+
		"\u0146\7g\2\2\u0146\u0147\7e\2\2\u0147\u0148\7k\2\2\u0148\u0149\7o\2\2"+
		"\u0149\u014a\7c\2\2\u014a\u014b\7n\2\2\u014b:\3\2\2\2\u014c\u014d\7u\2"+
		"\2\u014d\u014e\7v\2\2\u014e\u014f\7t\2\2\u014f\u0150\7k\2\2\u0150\u0151"+
		"\7p\2\2\u0151\u0152\7i\2\2\u0152<\3\2\2\2\u0153\u0154\7d\2\2\u0154\u0155"+
		"\7q\2\2\u0155\u0156\7q\2\2\u0156\u0157\7n\2\2\u0157\u0158\7g\2\2\u0158"+
		"\u0159\7c\2\2\u0159\u015a\7p\2\2\u015a>\3\2\2\2\u015b\u015c\7x\2\2\u015c"+
		"\u015d\7g\2\2\u015d\u015e\7e\2\2\u015e\u015f\7v\2\2\u015f\u0160\7q\2\2"+
		"\u0160\u0161\7t\2\2\u0161@\3\2\2\2\u0162\u0163\7n\2\2\u0163\u0164\7k\2"+
		"\2\u0164\u0165\7u\2\2\u0165\u0166\7v\2\2\u0166B\3\2\2\2\u0167\u0168\7"+
		"v\2\2\u0168\u0169\7t\2\2\u0169\u016a\7w\2\2\u016a\u016b\7g\2\2\u016bD"+
		"\3\2\2\2\u016c\u016d\7h\2\2\u016d\u016e\7c\2\2\u016e\u016f\7n\2\2\u016f"+
		"\u0170\7u\2\2\u0170\u0171\7g\2\2\u0171F\3\2\2\2\u0172\u0173\7z\2\2\u0173"+
		"H\3\2\2\2\u0174\u0175\7{\2\2\u0175J\3\2\2\2\u0176\u0177\7|\2\2\u0177L"+
		"\3\2\2\2\u0178\u0179\7,\2\2\u0179N\3\2\2\2\u017a\u017b\7\61\2\2\u017b"+
		"P\3\2\2\2\u017c\u017d\7-\2\2\u017dR\3\2\2\2\u017e\u017f\7/\2\2\u017fT"+
		"\3\2\2\2\u0180\u0181\7(\2\2\u0181V\3\2\2\2\u0182\u0183\7@\2\2\u0183X\3"+
		"\2\2\2\u0184\u0185\7@\2\2\u0185\u0186\7?\2\2\u0186Z\3\2\2\2\u0187\u0188"+
		"\7>\2\2\u0188\\\3\2\2\2\u0189\u018a\7>\2\2\u018a\u018b\7?\2\2\u018b^\3"+
		"\2\2\2\u018c\u018d\7?\2\2\u018d\u018e\7?\2\2\u018e`\3\2\2\2\u018f\u0190"+
		"\7?\2\2\u0190\u0191\7\61\2\2\u0191\u0192\7?\2\2\u0192b\3\2\2\2\u0193\u0194"+
		"\7p\2\2\u0194\u0195\7q\2\2\u0195\u0196\7v\2\2\u0196d\3\2\2\2\u0197\u0198"+
		"\7c\2\2\u0198\u0199\7p\2\2\u0199\u019a\7f\2\2\u019af\3\2\2\2\u019b\u019c"+
		"\7q\2\2\u019c\u019d\7t\2\2\u019dh\3\2\2\2\u019e\u019f\7*\2\2\u019fj\3"+
		"\2\2\2\u01a0\u01a1\7+\2\2\u01a1l\3\2\2\2\u01a2\u01a3\7]\2\2\u01a3n\3\2"+
		"\2\2\u01a4\u01a5\7_\2\2\u01a5p\3\2\2\2\u01a6\u01a7\7}\2\2\u01a7r\3\2\2"+
		"\2\u01a8\u01a9\7\177\2\2\u01a9t\3\2\2\2\u01aa\u01ab\7\60\2\2\u01abv\3"+
		"\2\2\2\u01ac\u01ad\7.\2\2\u01adx\3\2\2\2\u01ae\u01af\7=\2\2\u01afz\3\2"+
		"\2\2\u01b0\u01b1\7>\2\2\u01b1\u01b2\7/\2\2\u01b2|\3\2\2\2\u01b3\u01b4"+
		"\t\2\2\2\u01b4~\3\2\2\2\u01b5\u01b6\t\3\2\2\u01b6\u0080\3\2\2\2\u01b7"+
		"\u01b8\t\4\2\2\u01b8\u0082\3\2\2\2\u01b9\u01ba\7a\2\2\u01ba\u0084\3\2"+
		"\2\2\u01bb\u01bf\7%\2\2\u01bc\u01be\n\5\2\2\u01bd\u01bc\3\2\2\2\u01be"+
		"\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3\2"+
		"\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\t\5\2\2\u01c3\u01c4\3\2\2\2\u01c4"+
		"\u01c5\bC\2\2\u01c5\u0086\3\2\2\2\u01c6\u01c8\t\6\2\2\u01c7\u01c6\3\2"+
		"\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca"+
		"\u01cb\3\2\2\2\u01cb\u01cc\bD\2\2\u01cc\u0088\3\2\2\2\u01cd\u01d1\5\u0083"+
		"B\2\u01ce\u01d1\5\177@\2\u01cf\u01d1\5\u0081A\2\u01d0\u01cd\3\2\2\2\u01d0"+
		"\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d8\3\2\2\2\u01d2\u01d7\5\u0083"+
		"B\2\u01d3\u01d7\5\177@\2\u01d4\u01d7\5\u0081A\2\u01d5\u01d7\5}?\2\u01d6"+
		"\u01d2\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2"+
		"\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9"+
		"\u008a\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dd\5}?\2\u01dc\u01db\3\2\2"+
		"\2\u01dd\u01de\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u008c"+
		"\3\2\2\2\u01e0\u01e2\t\7\2\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2"+
		"\u01e3\3\2\2\2\u01e3\u01e4\5\u008bF\2\u01e4\u008e\3\2\2\2\u01e5\u01e6"+
		"\5\u008bF\2\u01e6\u01e8\7\60\2\2\u01e7\u01e9\5\u008bF\2\u01e8\u01e7\3"+
		"\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ed\3\2\2\2\u01ea\u01eb\7\60\2\2\u01eb"+
		"\u01ed\5\u008bF\2\u01ec\u01e5\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u0090"+
		"\3\2\2\2\u01ee\u01ef\t\b\2\2\u01ef\u01f0\5\u008dG\2\u01f0\u0092\3\2\2"+
		"\2\u01f1\u01f2\5\u008bF\2\u01f2\u01f3\5\u0091I\2\u01f3\u01f9\3\2\2\2\u01f4"+
		"\u01f6\5\u008fH\2\u01f5\u01f7\5\u0091I\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7"+
		"\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f1\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f9"+
		"\u0094\3\2\2\2\u01fa\u01fc\t\7\2\2\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3\2"+
		"\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\5\u0093J\2\u01fe\u0096\3\2\2\2\u01ff"+
		"\u0200\7$\2\2\u0200\u0098\3\2\2\2\u0201\u0202\7^\2\2\u0202\u0212\7\62"+
		"\2\2\u0203\u0204\7^\2\2\u0204\u0212\7d\2\2\u0205\u0206\7^\2\2\u0206\u0212"+
		"\7p\2\2\u0207\u0208\7^\2\2\u0208\u0212\7h\2\2\u0209\u020a\7^\2\2\u020a"+
		"\u0212\7t\2\2\u020b\u020c\7^\2\2\u020c\u0212\5\u0097L\2\u020d\u020e\7"+
		"^\2\2\u020e\u0212\7)\2\2\u020f\u0210\7^\2\2\u0210\u0212\7^\2\2\u0211\u0201"+
		"\3\2\2\2\u0211\u0203\3\2\2\2\u0211\u0205\3\2\2\2\u0211\u0207\3\2\2\2\u0211"+
		"\u0209\3\2\2\2\u0211\u020b\3\2\2\2\u0211\u020d\3\2\2\2\u0211\u020f\3\2"+
		"\2\2\u0212\u009a\3\2\2\2\u0213\u0216\n\t\2\2\u0214\u0216\5\u0099M\2\u0215"+
		"\u0213\3\2\2\2\u0215\u0214\3\2\2\2\u0216\u009c\3\2\2\2\u0217\u021b\5\u0097"+
		"L\2\u0218\u021a\5\u009bN\2\u0219\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b"+
		"\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b\3\2"+
		"\2\2\u021e\u021f\5\u0097L\2\u021f\u009e\3\2\2\2\22\2\u01bf\u01c9\u01d0"+
		"\u01d6\u01d8\u01de\u01e1\u01e8\u01ec\u01f6\u01f8\u01fb\u0211\u0215\u021b"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}