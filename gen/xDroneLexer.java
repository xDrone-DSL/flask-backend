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
		SIZE=16, IF=17, ELSE=18, WHILE=19, FOR=20, FROM=21, TO=22, STEP=23, REPEAT=24, 
		TIMES=25, DEL=26, FUNCTION=27, PROCEDURE=28, RETURN=29, TYPE_INT=30, TYPE_DECIMAL=31, 
		TYPE_STRING=32, TYPE_BOOLEAN=33, TYPE_VECTOR=34, TYPE_LIST=35, TRUE=36, 
		FALSE=37, VEC_X=38, VEC_Y=39, VEC_Z=40, MULTI=41, DIV=42, PLUS=43, MINUS=44, 
		CONCAT=45, GREATER=46, GREATER_EQ=47, LESS=48, LESS_EQ=49, EQ=50, NOT_EQ=51, 
		NOT=52, AND=53, OR=54, L_PAR=55, R_PAR=56, L_BRACKET=57, R_BRACKET=58, 
		L_BRACE=59, R_BRACE=60, DOT=61, COMMA=62, SEMICOLON=63, ARROW=64, COMMENT=65, 
		WS=66, IDENT=67, SIGNED_INT=68, SIGNED_FLOAT=69, ESCAPED_STRING=70;
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
			"SIZE", "IF", "ELSE", "WHILE", "FOR", "FROM", "TO", "STEP", "REPEAT", 
			"TIMES", "DEL", "FUNCTION", "PROCEDURE", "RETURN", "TYPE_INT", "TYPE_DECIMAL", 
			"TYPE_STRING", "TYPE_BOOLEAN", "TYPE_VECTOR", "TYPE_LIST", "TRUE", "FALSE", 
			"VEC_X", "VEC_Y", "VEC_Z", "MULTI", "DIV", "PLUS", "MINUS", "CONCAT", 
			"GREATER", "GREATER_EQ", "LESS", "LESS_EQ", "EQ", "NOT_EQ", "NOT", "AND", 
			"OR", "L_PAR", "R_PAR", "L_BRACKET", "R_BRACKET", "L_BRACE", "R_BRACE", 
			"DOT", "COMMA", "SEMICOLON", "ARROW", "DIGIT", "LOWERCASE", "UPPERCASE", 
			"UNDERSCORE", "COMMENT", "WS", "IDENT", "INT", "SIGNED_INT", "DECIMAL", 
			"EXP", "FLOAT", "SIGNED_FLOAT", "DOUBLE_QUOTE", "ESCAPED_CHAR", "CHARACTER", 
			"ESCAPED_STRING"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'main'", "'takeoff'", "'land'", "'up'", "'down'", "'left'", "'right'", 
			"'forward'", "'backward'", "'rotate_left'", "'rotate_right'", "'wait'", 
			"'at'", "'insert'", "'remove'", "'size'", "'if'", "'else'", "'while'", 
			"'for'", "'from'", "'to'", "'step'", "'repeat'", "'times'", "'del'", 
			"'function'", "'procedure'", "'return'", "'int'", "'decimal'", "'string'", 
			"'boolean'", "'vector'", "'list'", "'true'", "'false'", "'x'", "'y'", 
			"'z'", "'*'", "'/'", "'+'", "'-'", "'&'", "'>'", "'>='", "'<'", "'<='", 
			"'=='", "'=/='", "'not'", "'and'", "'or'", "'('", "')'", "'['", "']'", 
			"'{'", "'}'", "'.'", "','", "';'", "'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MAIN", "TAKEOFF", "LAND", "UP", "DOWN", "LEFT", "RIGHT", "FORWARD", 
			"BACKWARD", "ROTATE_LEFT", "ROTATE_RIGHT", "WAIT", "AT", "INSERT", "REMOVE", 
			"SIZE", "IF", "ELSE", "WHILE", "FOR", "FROM", "TO", "STEP", "REPEAT", 
			"TIMES", "DEL", "FUNCTION", "PROCEDURE", "RETURN", "TYPE_INT", "TYPE_DECIMAL", 
			"TYPE_STRING", "TYPE_BOOLEAN", "TYPE_VECTOR", "TYPE_LIST", "TRUE", "FALSE", 
			"VEC_X", "VEC_Y", "VEC_Z", "MULTI", "DIV", "PLUS", "MINUS", "CONCAT", 
			"GREATER", "GREATER_EQ", "LESS", "LESS_EQ", "EQ", "NOT_EQ", "NOT", "AND", 
			"OR", "L_PAR", "R_PAR", "L_BRACKET", "R_BRACKET", "L_BRACE", "R_BRACE", 
			"DOT", "COMMA", "SEMICOLON", "ARROW", "COMMENT", "WS", "IDENT", "SIGNED_INT", 
			"SIGNED_FLOAT", "ESCAPED_STRING"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H\u0239\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3"+
		"\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3"+
		"\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3"+
		"\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3"+
		"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3"+
		" \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3"+
		"\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&"+
		"\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3"+
		"\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3"+
		"\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3:\3"+
		":\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3"+
		"E\3F\3F\7F\u01d7\nF\fF\16F\u01da\13F\3F\3F\3F\3F\3G\6G\u01e1\nG\rG\16"+
		"G\u01e2\3G\3G\3H\3H\3H\5H\u01ea\nH\3H\3H\3H\3H\7H\u01f0\nH\fH\16H\u01f3"+
		"\13H\3I\6I\u01f6\nI\rI\16I\u01f7\3J\5J\u01fb\nJ\3J\3J\3K\3K\3K\5K\u0202"+
		"\nK\3K\3K\5K\u0206\nK\3L\3L\3L\3M\3M\3M\3M\3M\5M\u0210\nM\5M\u0212\nM"+
		"\3N\5N\u0215\nN\3N\3N\3O\3O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P"+
		"\3P\3P\5P\u022b\nP\3Q\3Q\5Q\u022f\nQ\3R\3R\7R\u0233\nR\fR\16R\u0236\13"+
		"R\3R\3R\2\2S\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16"+
		"\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34"+
		"\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g"+
		"\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083\2\u0085\2\u0087\2\u0089"+
		"\2\u008bC\u008dD\u008fE\u0091\2\u0093F\u0095\2\u0097\2\u0099\2\u009bG"+
		"\u009d\2\u009f\2\u00a1\2\u00a3H\3\2\n\3\2\62;\3\2c|\3\2C\\\4\2\f\f\17"+
		"\17\5\2\13\f\17\17\"\"\4\2--//\4\2GGgg\5\2$$))^^\2\u0245\2\3\3\2\2\2\2"+
		"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2"+
		"\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2"+
		"\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2"+
		"\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2"+
		"\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2"+
		"\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2"+
		"K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3"+
		"\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2"+
		"\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2"+
		"q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3"+
		"\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2"+
		"\u008f\3\2\2\2\2\u0093\3\2\2\2\2\u009b\3\2\2\2\2\u00a3\3\2\2\2\3\u00a5"+
		"\3\2\2\2\5\u00aa\3\2\2\2\7\u00b2\3\2\2\2\t\u00b7\3\2\2\2\13\u00ba\3\2"+
		"\2\2\r\u00bf\3\2\2\2\17\u00c4\3\2\2\2\21\u00ca\3\2\2\2\23\u00d2\3\2\2"+
		"\2\25\u00db\3\2\2\2\27\u00e7\3\2\2\2\31\u00f4\3\2\2\2\33\u00f9\3\2\2\2"+
		"\35\u00fc\3\2\2\2\37\u0103\3\2\2\2!\u010a\3\2\2\2#\u010f\3\2\2\2%\u0112"+
		"\3\2\2\2\'\u0117\3\2\2\2)\u011d\3\2\2\2+\u0121\3\2\2\2-\u0126\3\2\2\2"+
		"/\u0129\3\2\2\2\61\u012e\3\2\2\2\63\u0135\3\2\2\2\65\u013b\3\2\2\2\67"+
		"\u013f\3\2\2\29\u0148\3\2\2\2;\u0152\3\2\2\2=\u0159\3\2\2\2?\u015d\3\2"+
		"\2\2A\u0165\3\2\2\2C\u016c\3\2\2\2E\u0174\3\2\2\2G\u017b\3\2\2\2I\u0180"+
		"\3\2\2\2K\u0185\3\2\2\2M\u018b\3\2\2\2O\u018d\3\2\2\2Q\u018f\3\2\2\2S"+
		"\u0191\3\2\2\2U\u0193\3\2\2\2W\u0195\3\2\2\2Y\u0197\3\2\2\2[\u0199\3\2"+
		"\2\2]\u019b\3\2\2\2_\u019d\3\2\2\2a\u01a0\3\2\2\2c\u01a2\3\2\2\2e\u01a5"+
		"\3\2\2\2g\u01a8\3\2\2\2i\u01ac\3\2\2\2k\u01b0\3\2\2\2m\u01b4\3\2\2\2o"+
		"\u01b7\3\2\2\2q\u01b9\3\2\2\2s\u01bb\3\2\2\2u\u01bd\3\2\2\2w\u01bf\3\2"+
		"\2\2y\u01c1\3\2\2\2{\u01c3\3\2\2\2}\u01c5\3\2\2\2\177\u01c7\3\2\2\2\u0081"+
		"\u01c9\3\2\2\2\u0083\u01cc\3\2\2\2\u0085\u01ce\3\2\2\2\u0087\u01d0\3\2"+
		"\2\2\u0089\u01d2\3\2\2\2\u008b\u01d4\3\2\2\2\u008d\u01e0\3\2\2\2\u008f"+
		"\u01e9\3\2\2\2\u0091\u01f5\3\2\2\2\u0093\u01fa\3\2\2\2\u0095\u0205\3\2"+
		"\2\2\u0097\u0207\3\2\2\2\u0099\u0211\3\2\2\2\u009b\u0214\3\2\2\2\u009d"+
		"\u0218\3\2\2\2\u009f\u022a\3\2\2\2\u00a1\u022e\3\2\2\2\u00a3\u0230\3\2"+
		"\2\2\u00a5\u00a6\7o\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9"+
		"\7p\2\2\u00a9\4\3\2\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad"+
		"\7m\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7h\2\2\u00b0"+
		"\u00b1\7h\2\2\u00b1\6\3\2\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7c\2\2\u00b4"+
		"\u00b5\7p\2\2\u00b5\u00b6\7f\2\2\u00b6\b\3\2\2\2\u00b7\u00b8\7w\2\2\u00b8"+
		"\u00b9\7r\2\2\u00b9\n\3\2\2\2\u00ba\u00bb\7f\2\2\u00bb\u00bc\7q\2\2\u00bc"+
		"\u00bd\7y\2\2\u00bd\u00be\7p\2\2\u00be\f\3\2\2\2\u00bf\u00c0\7n\2\2\u00c0"+
		"\u00c1\7g\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7v\2\2\u00c3\16\3\2\2\2\u00c4"+
		"\u00c5\7t\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7i\2\2\u00c7\u00c8\7j\2\2"+
		"\u00c8\u00c9\7v\2\2\u00c9\20\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7"+
		"q\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7y\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0"+
		"\7t\2\2\u00d0\u00d1\7f\2\2\u00d1\22\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4"+
		"\7c\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6\7m\2\2\u00d6\u00d7\7y\2\2\u00d7"+
		"\u00d8\7c\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7f\2\2\u00da\24\3\2\2\2\u00db"+
		"\u00dc\7t\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7c\2\2"+
		"\u00df\u00e0\7v\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7a\2\2\u00e2\u00e3"+
		"\7n\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6\7v\2\2\u00e6"+
		"\26\3\2\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7v\2\2\u00ea"+
		"\u00eb\7c\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7a\2\2"+
		"\u00ee\u00ef\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7i\2\2\u00f1\u00f2"+
		"\7j\2\2\u00f2\u00f3\7v\2\2\u00f3\30\3\2\2\2\u00f4\u00f5\7y\2\2\u00f5\u00f6"+
		"\7c\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7v\2\2\u00f8\32\3\2\2\2\u00f9\u00fa"+
		"\7c\2\2\u00fa\u00fb\7v\2\2\u00fb\34\3\2\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe"+
		"\7p\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7t\2\2\u0101"+
		"\u0102\7v\2\2\u0102\36\3\2\2\2\u0103\u0104\7t\2\2\u0104\u0105\7g\2\2\u0105"+
		"\u0106\7o\2\2\u0106\u0107\7q\2\2\u0107\u0108\7x\2\2\u0108\u0109\7g\2\2"+
		"\u0109 \3\2\2\2\u010a\u010b\7u\2\2\u010b\u010c\7k\2\2\u010c\u010d\7|\2"+
		"\2\u010d\u010e\7g\2\2\u010e\"\3\2\2\2\u010f\u0110\7k\2\2\u0110\u0111\7"+
		"h\2\2\u0111$\3\2\2\2\u0112\u0113\7g\2\2\u0113\u0114\7n\2\2\u0114\u0115"+
		"\7u\2\2\u0115\u0116\7g\2\2\u0116&\3\2\2\2\u0117\u0118\7y\2\2\u0118\u0119"+
		"\7j\2\2\u0119\u011a\7k\2\2\u011a\u011b\7n\2\2\u011b\u011c\7g\2\2\u011c"+
		"(\3\2\2\2\u011d\u011e\7h\2\2\u011e\u011f\7q\2\2\u011f\u0120\7t\2\2\u0120"+
		"*\3\2\2\2\u0121\u0122\7h\2\2\u0122\u0123\7t\2\2\u0123\u0124\7q\2\2\u0124"+
		"\u0125\7o\2\2\u0125,\3\2\2\2\u0126\u0127\7v\2\2\u0127\u0128\7q\2\2\u0128"+
		".\3\2\2\2\u0129\u012a\7u\2\2\u012a\u012b\7v\2\2\u012b\u012c\7g\2\2\u012c"+
		"\u012d\7r\2\2\u012d\60\3\2\2\2\u012e\u012f\7t\2\2\u012f\u0130\7g\2\2\u0130"+
		"\u0131\7r\2\2\u0131\u0132\7g\2\2\u0132\u0133\7c\2\2\u0133\u0134\7v\2\2"+
		"\u0134\62\3\2\2\2\u0135\u0136\7v\2\2\u0136\u0137\7k\2\2\u0137\u0138\7"+
		"o\2\2\u0138\u0139\7g\2\2\u0139\u013a\7u\2\2\u013a\64\3\2\2\2\u013b\u013c"+
		"\7f\2\2\u013c\u013d\7g\2\2\u013d\u013e\7n\2\2\u013e\66\3\2\2\2\u013f\u0140"+
		"\7h\2\2\u0140\u0141\7w\2\2\u0141\u0142\7p\2\2\u0142\u0143\7e\2\2\u0143"+
		"\u0144\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146\7q\2\2\u0146\u0147\7p\2\2"+
		"\u01478\3\2\2\2\u0148\u0149\7r\2\2\u0149\u014a\7t\2\2\u014a\u014b\7q\2"+
		"\2\u014b\u014c\7e\2\2\u014c\u014d\7g\2\2\u014d\u014e\7f\2\2\u014e\u014f"+
		"\7w\2\2\u014f\u0150\7t\2\2\u0150\u0151\7g\2\2\u0151:\3\2\2\2\u0152\u0153"+
		"\7t\2\2\u0153\u0154\7g\2\2\u0154\u0155\7v\2\2\u0155\u0156\7w\2\2\u0156"+
		"\u0157\7t\2\2\u0157\u0158\7p\2\2\u0158<\3\2\2\2\u0159\u015a\7k\2\2\u015a"+
		"\u015b\7p\2\2\u015b\u015c\7v\2\2\u015c>\3\2\2\2\u015d\u015e\7f\2\2\u015e"+
		"\u015f\7g\2\2\u015f\u0160\7e\2\2\u0160\u0161\7k\2\2\u0161\u0162\7o\2\2"+
		"\u0162\u0163\7c\2\2\u0163\u0164\7n\2\2\u0164@\3\2\2\2\u0165\u0166\7u\2"+
		"\2\u0166\u0167\7v\2\2\u0167\u0168\7t\2\2\u0168\u0169\7k\2\2\u0169\u016a"+
		"\7p\2\2\u016a\u016b\7i\2\2\u016bB\3\2\2\2\u016c\u016d\7d\2\2\u016d\u016e"+
		"\7q\2\2\u016e\u016f\7q\2\2\u016f\u0170\7n\2\2\u0170\u0171\7g\2\2\u0171"+
		"\u0172\7c\2\2\u0172\u0173\7p\2\2\u0173D\3\2\2\2\u0174\u0175\7x\2\2\u0175"+
		"\u0176\7g\2\2\u0176\u0177\7e\2\2\u0177\u0178\7v\2\2\u0178\u0179\7q\2\2"+
		"\u0179\u017a\7t\2\2\u017aF\3\2\2\2\u017b\u017c\7n\2\2\u017c\u017d\7k\2"+
		"\2\u017d\u017e\7u\2\2\u017e\u017f\7v\2\2\u017fH\3\2\2\2\u0180\u0181\7"+
		"v\2\2\u0181\u0182\7t\2\2\u0182\u0183\7w\2\2\u0183\u0184\7g\2\2\u0184J"+
		"\3\2\2\2\u0185\u0186\7h\2\2\u0186\u0187\7c\2\2\u0187\u0188\7n\2\2\u0188"+
		"\u0189\7u\2\2\u0189\u018a\7g\2\2\u018aL\3\2\2\2\u018b\u018c\7z\2\2\u018c"+
		"N\3\2\2\2\u018d\u018e\7{\2\2\u018eP\3\2\2\2\u018f\u0190\7|\2\2\u0190R"+
		"\3\2\2\2\u0191\u0192\7,\2\2\u0192T\3\2\2\2\u0193\u0194\7\61\2\2\u0194"+
		"V\3\2\2\2\u0195\u0196\7-\2\2\u0196X\3\2\2\2\u0197\u0198\7/\2\2\u0198Z"+
		"\3\2\2\2\u0199\u019a\7(\2\2\u019a\\\3\2\2\2\u019b\u019c\7@\2\2\u019c^"+
		"\3\2\2\2\u019d\u019e\7@\2\2\u019e\u019f\7?\2\2\u019f`\3\2\2\2\u01a0\u01a1"+
		"\7>\2\2\u01a1b\3\2\2\2\u01a2\u01a3\7>\2\2\u01a3\u01a4\7?\2\2\u01a4d\3"+
		"\2\2\2\u01a5\u01a6\7?\2\2\u01a6\u01a7\7?\2\2\u01a7f\3\2\2\2\u01a8\u01a9"+
		"\7?\2\2\u01a9\u01aa\7\61\2\2\u01aa\u01ab\7?\2\2\u01abh\3\2\2\2\u01ac\u01ad"+
		"\7p\2\2\u01ad\u01ae\7q\2\2\u01ae\u01af\7v\2\2\u01afj\3\2\2\2\u01b0\u01b1"+
		"\7c\2\2\u01b1\u01b2\7p\2\2\u01b2\u01b3\7f\2\2\u01b3l\3\2\2\2\u01b4\u01b5"+
		"\7q\2\2\u01b5\u01b6\7t\2\2\u01b6n\3\2\2\2\u01b7\u01b8\7*\2\2\u01b8p\3"+
		"\2\2\2\u01b9\u01ba\7+\2\2\u01bar\3\2\2\2\u01bb\u01bc\7]\2\2\u01bct\3\2"+
		"\2\2\u01bd\u01be\7_\2\2\u01bev\3\2\2\2\u01bf\u01c0\7}\2\2\u01c0x\3\2\2"+
		"\2\u01c1\u01c2\7\177\2\2\u01c2z\3\2\2\2\u01c3\u01c4\7\60\2\2\u01c4|\3"+
		"\2\2\2\u01c5\u01c6\7.\2\2\u01c6~\3\2\2\2\u01c7\u01c8\7=\2\2\u01c8\u0080"+
		"\3\2\2\2\u01c9\u01ca\7>\2\2\u01ca\u01cb\7/\2\2\u01cb\u0082\3\2\2\2\u01cc"+
		"\u01cd\t\2\2\2\u01cd\u0084\3\2\2\2\u01ce\u01cf\t\3\2\2\u01cf\u0086\3\2"+
		"\2\2\u01d0\u01d1\t\4\2\2\u01d1\u0088\3\2\2\2\u01d2\u01d3\7a\2\2\u01d3"+
		"\u008a\3\2\2\2\u01d4\u01d8\7%\2\2\u01d5\u01d7\n\5\2\2\u01d6\u01d5\3\2"+
		"\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9"+
		"\u01db\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dc\t\5\2\2\u01dc\u01dd\3\2"+
		"\2\2\u01dd\u01de\bF\2\2\u01de\u008c\3\2\2\2\u01df\u01e1\t\6\2\2\u01e0"+
		"\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2"+
		"\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\bG\2\2\u01e5\u008e\3\2\2\2\u01e6"+
		"\u01ea\5\u0089E\2\u01e7\u01ea\5\u0085C\2\u01e8\u01ea\5\u0087D\2\u01e9"+
		"\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01f1\3\2"+
		"\2\2\u01eb\u01f0\5\u0089E\2\u01ec\u01f0\5\u0085C\2\u01ed\u01f0\5\u0087"+
		"D\2\u01ee\u01f0\5\u0083B\2\u01ef\u01eb\3\2\2\2\u01ef\u01ec\3\2\2\2\u01ef"+
		"\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2"+
		"\2\2\u01f1\u01f2\3\2\2\2\u01f2\u0090\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4"+
		"\u01f6\5\u0083B\2\u01f5\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5"+
		"\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u0092\3\2\2\2\u01f9\u01fb\t\7\2\2\u01fa"+
		"\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\5\u0091"+
		"I\2\u01fd\u0094\3\2\2\2\u01fe\u01ff\5\u0091I\2\u01ff\u0201\7\60\2\2\u0200"+
		"\u0202\5\u0091I\2\u0201\u0200\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0206"+
		"\3\2\2\2\u0203\u0204\7\60\2\2\u0204\u0206\5\u0091I\2\u0205\u01fe\3\2\2"+
		"\2\u0205\u0203\3\2\2\2\u0206\u0096\3\2\2\2\u0207\u0208\t\b\2\2\u0208\u0209"+
		"\5\u0093J\2\u0209\u0098\3\2\2\2\u020a\u020b\5\u0091I\2\u020b\u020c\5\u0097"+
		"L\2\u020c\u0212\3\2\2\2\u020d\u020f\5\u0095K\2\u020e\u0210\5\u0097L\2"+
		"\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u020a"+
		"\3\2\2\2\u0211\u020d\3\2\2\2\u0212\u009a\3\2\2\2\u0213\u0215\t\7\2\2\u0214"+
		"\u0213\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\5\u0099"+
		"M\2\u0217\u009c\3\2\2\2\u0218\u0219\7$\2\2\u0219\u009e\3\2\2\2\u021a\u021b"+
		"\7^\2\2\u021b\u022b\7\62\2\2\u021c\u021d\7^\2\2\u021d\u022b\7d\2\2\u021e"+
		"\u021f\7^\2\2\u021f\u022b\7p\2\2\u0220\u0221\7^\2\2\u0221\u022b\7h\2\2"+
		"\u0222\u0223\7^\2\2\u0223\u022b\7t\2\2\u0224\u0225\7^\2\2\u0225\u022b"+
		"\5\u009dO\2\u0226\u0227\7^\2\2\u0227\u022b\7)\2\2\u0228\u0229\7^\2\2\u0229"+
		"\u022b\7^\2\2\u022a\u021a\3\2\2\2\u022a\u021c\3\2\2\2\u022a\u021e\3\2"+
		"\2\2\u022a\u0220\3\2\2\2\u022a\u0222\3\2\2\2\u022a\u0224\3\2\2\2\u022a"+
		"\u0226\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u00a0\3\2\2\2\u022c\u022f\n\t"+
		"\2\2\u022d\u022f\5\u009fP\2\u022e\u022c\3\2\2\2\u022e\u022d\3\2\2\2\u022f"+
		"\u00a2\3\2\2\2\u0230\u0234\5\u009dO\2\u0231\u0233\5\u00a1Q\2\u0232\u0231"+
		"\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235"+
		"\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\5\u009dO\2\u0238\u00a4"+
		"\3\2\2\2\22\2\u01d8\u01e2\u01e9\u01ef\u01f1\u01f7\u01fa\u0201\u0205\u020f"+
		"\u0211\u0214\u022a\u022e\u0234\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}