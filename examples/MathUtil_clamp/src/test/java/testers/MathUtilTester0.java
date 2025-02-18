package testers;

import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class MathUtilTester0 {

    public static boolean debug = false;

    @Test
    public void test001() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test001");
        jts.MathUtil mathUtil0 = new jts.MathUtil();
        java.lang.Class<?> wildcardClass1 = mathUtil0.getClass();
    }

    @Test
    public void test002() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test002");
        int int3 = jts.MathUtil.clamp((-3), (int) (byte) 1, 9);
    }

    @Test
    public void test003() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test003");
        int int3 = jts.MathUtil.clamp((int) 'a', (-2), (int) (byte) 1);
    }

    @Test
    public void test004() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test004");
        int int3 = jts.MathUtil.clamp(0, 6, 9);
    }

    @Test
    public void test005() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test005");
        int int3 = jts.MathUtil.clamp(100, (int) '4', (int) (byte) -1);
    }

    @Test
    public void test006() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test006");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 100, (int) '4');
    }

    @Test
    public void test007() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test007");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (-2), (-7));
    }

    @Test
    public void test008() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test008");
        int int3 = jts.MathUtil.clamp(7, (int) (short) 1, (int) (byte) 10);
    }

    @Test
    public void test009() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test009");
        java.lang.Object obj0 = new java.lang.Object();
        java.lang.Class<?> wildcardClass1 = obj0.getClass();
    }

    @Test
    public void test010() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test010");
        int int3 = jts.MathUtil.clamp((int) (short) 10, (-9), 1);
    }

    @Test
    public void test011() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test011");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (-7), 0);
    }

    @Test
    public void test012() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test012");
        int int3 = jts.MathUtil.clamp((-5), 0, 2);
    }

    @Test
    public void test013() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test013");
        int int3 = jts.MathUtil.clamp(4, (-9), (int) 'a');
    }

    @Test
    public void test014() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test014");
        int int3 = jts.MathUtil.clamp(0, 0, (-10));
    }

    @Test
    public void test015() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test015");
        int int3 = jts.MathUtil.clamp((int) 'a', (int) '4', (-100));
    }

    @Test
    public void test016() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test016");
        int int3 = jts.MathUtil.clamp((-3), (int) 'a', (-1));
    }

    @Test
    public void test017() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test017");
        int int3 = jts.MathUtil.clamp(5, 2, 1);
    }

    @Test
    public void test018() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test018");
        int int3 = jts.MathUtil.clamp(10, 0, 0);
    }

    @Test
    public void test019() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test019");
        int int3 = jts.MathUtil.clamp((-9), (int) '4', 4);
    }

    @Test
    public void test020() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test020");
        int int3 = jts.MathUtil.clamp(1, 4, 10);
    }

    @Test
    public void test021() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test021");
        int int3 = jts.MathUtil.clamp(100, 100, (-6));
    }

    @Test
    public void test022() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test022");
        int int3 = jts.MathUtil.clamp(8, (-4), (int) '#');
    }

    @Test
    public void test023() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test023");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 1, (-3));
    }

    @Test
    public void test024() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test024");
        int int3 = jts.MathUtil.clamp(52, 0, 8);
    }

    @Test
    public void test025() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test025");
        int int3 = jts.MathUtil.clamp(10, 7, 97);
    }

    @Test
    public void test026() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test026");
        int int3 = jts.MathUtil.clamp(2, 52, (int) (short) 10);
    }

    @Test
    public void test027() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test027");
        int int3 = jts.MathUtil.clamp(10, (int) (short) 1, (-9));
    }

    @Test
    public void test028() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test028");
        int int3 = jts.MathUtil.clamp(4, 0, (-10));
    }

    @Test
    public void test029() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test029");
        int int3 = jts.MathUtil.clamp((int) (short) 1, (int) (byte) 10, (-2));
    }

    @Test
    public void test030() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test030");
        int int3 = jts.MathUtil.clamp(0, (-3), (-1));
    }

    @Test
    public void test031() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test031");
        int int3 = jts.MathUtil.clamp(5, 100, 8);
    }

    @Test
    public void test032() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test032");
        int int3 = jts.MathUtil.clamp((-6), (-100), (int) (short) 0);
    }

    @Test
    public void test033() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test033");
        int int3 = jts.MathUtil.clamp((int) (short) 0, 100, (-1));
    }

    @Test
    public void test034() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test034");
        int int3 = jts.MathUtil.clamp(10, 4, 4);
    }

    @Test
    public void test035() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test035");
        int int3 = jts.MathUtil.clamp(1, (-8), (-3));
    }

    @Test
    public void test036() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test036");
        int int3 = jts.MathUtil.clamp(100, (int) (short) 100, (-9));
    }

    @Test
    public void test037() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test037");
        int int3 = jts.MathUtil.clamp(1, 0, 7);
    }

    @Test
    public void test038() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test038");
        int int3 = jts.MathUtil.clamp((-1), 4, (-7));
    }

    @Test
    public void test039() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test039");
        int int3 = jts.MathUtil.clamp((int) '4', 10, 4);
    }

    @Test
    public void test040() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test040");
        int int3 = jts.MathUtil.clamp(0, (int) (short) 0, 97);
    }

    @Test
    public void test041() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test041");
        int int3 = jts.MathUtil.clamp((int) ' ', (int) (byte) 1, 0);
    }

    @Test
    public void test042() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test042");
        int int3 = jts.MathUtil.clamp(0, (-10), 0);
    }

    @Test
    public void test043() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test043");
        int int3 = jts.MathUtil.clamp(0, 97, (-6));
    }

    @Test
    public void test044() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test044");
        int int3 = jts.MathUtil.clamp(1, (int) (short) 1, (-4));
    }

    @Test
    public void test045() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test045");
        int int3 = jts.MathUtil.clamp(100, (-7), 8);
    }

    @Test
    public void test046() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test046");
        int int3 = jts.MathUtil.clamp(52, 10, (int) (short) 0);
    }

    @Test
    public void test047() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test047");
        int int3 = jts.MathUtil.clamp(10, 9, (-4));
    }

    @Test
    public void test048() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test048");
        int int3 = jts.MathUtil.clamp(52, (int) (short) 1, 4);
    }

    @Test
    public void test049() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test049");
        int int3 = jts.MathUtil.clamp((-100), (int) '#', (int) (short) 10);
    }

    @Test
    public void test050() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test050");
        int int3 = jts.MathUtil.clamp(10, 4, (-6));
    }

    @Test
    public void test051() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test051");
        int int3 = jts.MathUtil.clamp((int) ' ', (int) 'a', 6);
    }

    @Test
    public void test052() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test052");
        int int3 = jts.MathUtil.clamp(97, (-10), 10);
    }

    @Test
    public void test053() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test053");
        int int3 = jts.MathUtil.clamp(9, (-8), 1);
    }

    @Test
    public void test054() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test054");
        int int3 = jts.MathUtil.clamp((-5), 52, 0);
    }

    @Test
    public void test055() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test055");
        int int3 = jts.MathUtil.clamp(6, 0, (int) (short) 10);
    }

    @Test
    public void test056() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test056");
        int int3 = jts.MathUtil.clamp(52, (int) (short) -1, (-10));
    }

    @Test
    public void test057() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test057");
        int int3 = jts.MathUtil.clamp(7, (int) '#', (int) (byte) 1);
    }

    @Test
    public void test058() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test058");
        int int3 = jts.MathUtil.clamp(10, (int) (short) 10, (-5));
    }

    @Test
    public void test059() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test059");
        int int3 = jts.MathUtil.clamp((int) ' ', (int) '4', 7);
    }

    @Test
    public void test060() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test060");
        int int3 = jts.MathUtil.clamp((-8), 5, 0);
    }

    @Test
    public void test061() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test061");
        int int3 = jts.MathUtil.clamp(8, (int) (byte) 1, 0);
    }

    @Test
    public void test062() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test062");
        int int3 = jts.MathUtil.clamp((-7), (int) (short) 100, 5);
    }

    @Test
    public void test063() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test063");
        int int3 = jts.MathUtil.clamp((int) (short) 1, 4, 100);
    }

    @Test
    public void test064() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test064");
        int int3 = jts.MathUtil.clamp(3, 10, (-6));
    }

    @Test
    public void test065() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test065");
        int int3 = jts.MathUtil.clamp((-5), 97, (-7));
    }

    @Test
    public void test066() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test066");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 35, (-4));
    }

    @Test
    public void test067() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test067");
        int int3 = jts.MathUtil.clamp(10, 7, 0);
    }

    @Test
    public void test068() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test068");
        int int3 = jts.MathUtil.clamp(2, (int) (byte) 100, 0);
    }

    @Test
    public void test069() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test069");
        int int3 = jts.MathUtil.clamp(7, 10, 6);
    }

    @Test
    public void test070() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test070");
        int int3 = jts.MathUtil.clamp(35, 0, 10);
    }

    @Test
    public void test071() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test071");
        int int3 = jts.MathUtil.clamp((-10), 0, (-5));
    }

    @Test
    public void test072() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test072");
        int int3 = jts.MathUtil.clamp(5, (int) (short) 0, 9);
    }

    @Test
    public void test073() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test073");
        int int3 = jts.MathUtil.clamp(1, 7, 3);
    }

    @Test
    public void test074() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test074");
        int int3 = jts.MathUtil.clamp((-9), 3, 0);
    }

    @Test
    public void test075() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test075");
        int int3 = jts.MathUtil.clamp(10, (int) (short) -1, (int) (short) 0);
    }

    @Test
    public void test076() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test076");
        int int3 = jts.MathUtil.clamp(7, (int) (byte) 0, 3);
    }

    @Test
    public void test077() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test077");
        int int3 = jts.MathUtil.clamp(3, 10, (int) (byte) 10);
    }

    @Test
    public void test078() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test078");
        int int3 = jts.MathUtil.clamp((-6), 5, (int) (short) -1);
    }

    @Test
    public void test079() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test079");
        int int3 = jts.MathUtil.clamp(9, 10, (-2));
    }

    @Test
    public void test080() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test080");
        int int3 = jts.MathUtil.clamp(52, 0, (int) (byte) 0);
    }

    @Test
    public void test081() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test081");
        int int3 = jts.MathUtil.clamp(6, (int) (short) -1, (int) (short) 10);
    }

    @Test
    public void test082() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test082");
        int int3 = jts.MathUtil.clamp(6, (int) (byte) 100, 0);
    }

    @Test
    public void test083() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test083");
        int int3 = jts.MathUtil.clamp(7, 1, 1);
    }

    @Test
    public void test084() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test084");
        int int3 = jts.MathUtil.clamp(0, (-3), (int) (short) 1);
    }

    @Test
    public void test085() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test085");
        int int3 = jts.MathUtil.clamp(0, (int) (byte) 0, (int) (byte) 100);
    }

    @Test
    public void test086() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test086");
        int int3 = jts.MathUtil.clamp(0, (-9), 0);
    }

    @Test
    public void test087() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test087");
        int int3 = jts.MathUtil.clamp(1, 0, 9);
    }

    @Test
    public void test088() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test088");
        int int3 = jts.MathUtil.clamp((-100), 0, (-9));
    }

    @Test
    public void test089() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test089");
        int int3 = jts.MathUtil.clamp((int) '4', 100, (int) (byte) 0);
    }

    @Test
    public void test090() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test090");
        int int3 = jts.MathUtil.clamp(9, 7, (int) (short) -1);
    }

    @Test
    public void test091() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test091");
        int int3 = jts.MathUtil.clamp((-1), 10, (-2));
    }

    @Test
    public void test092() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test092");
        int int3 = jts.MathUtil.clamp((-1), (int) (byte) 100, (int) (byte) 1);
    }

    @Test
    public void test093() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test093");
        int int3 = jts.MathUtil.clamp(2, (int) (byte) 100, (int) (byte) 1);
    }

    @Test
    public void test094() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test094");
        int int3 = jts.MathUtil.clamp((int) (byte) 10, 10, (int) (short) 10);
    }

    @Test
    public void test095() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test095");
        int int3 = jts.MathUtil.clamp((-9), (int) (byte) 100, (int) (short) 0);
    }

    @Test
    public void test096() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test096");
        int int3 = jts.MathUtil.clamp((-9), (int) (byte) -1, (-10));
    }

    @Test
    public void test097() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test097");
        int int3 = jts.MathUtil.clamp(1, 4, 6);
    }

    @Test
    public void test098() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test098");
        int int3 = jts.MathUtil.clamp(0, (int) '4', (int) (byte) -1);
    }

    @Test
    public void test099() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test099");
        int int3 = jts.MathUtil.clamp((int) ' ', 5, 100);
    }

    @Test
    public void test100() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test100");
        int int3 = jts.MathUtil.clamp(97, 4, (int) (short) 10);
    }

    @Test
    public void test101() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test101");
        int int3 = jts.MathUtil.clamp(5, 7, (int) ' ');
    }

    @Test
    public void test102() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test102");
        int int3 = jts.MathUtil.clamp(6, (int) (byte) 1, 100);
    }

    @Test
    public void test103() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test103");
        int int3 = jts.MathUtil.clamp((int) '#', 32, (-8));
    }

    @Test
    public void test104() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test104");
        int int3 = jts.MathUtil.clamp(9, (int) '4', (-2));
    }

    @Test
    public void test105() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test105");
        int int3 = jts.MathUtil.clamp((-10), (int) 'a', 100);
    }

    @Test
    public void test106() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test106");
        int int3 = jts.MathUtil.clamp(97, (int) (byte) 1, (int) '#');
    }

    @Test
    public void test107() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test107");
        int int3 = jts.MathUtil.clamp((-2), 10, (int) '4');
    }

    @Test
    public void test108() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test108");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, 52, (-9));
    }

    @Test
    public void test109() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test109");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (-1), (-100));
    }

    @Test
    public void test110() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test110");
        int int3 = jts.MathUtil.clamp(0, 5, (-3));
    }

    @Test
    public void test111() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test111");
        int int3 = jts.MathUtil.clamp(0, 6, (-100));
    }

    @Test
    public void test112() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test112");
        int int3 = jts.MathUtil.clamp((int) 'a', 0, (-6));
    }

    @Test
    public void test113() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test113");
        int int3 = jts.MathUtil.clamp(32, (int) (short) 0, 10);
    }

    @Test
    public void test114() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test114");
        int int3 = jts.MathUtil.clamp(6, (int) (short) 0, (-100));
    }

    @Test
    public void test115() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test115");
        int int3 = jts.MathUtil.clamp(0, 7, (int) (byte) 1);
    }

    @Test
    public void test116() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test116");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (int) (byte) 10, (-100));
    }

    @Test
    public void test117() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test117");
        int int3 = jts.MathUtil.clamp((int) ' ', (int) (byte) 1, (-1));
    }

    @Test
    public void test118() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test118");
        int int3 = jts.MathUtil.clamp(10, 0, 35);
    }

    @Test
    public void test119() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test119");
        int int3 = jts.MathUtil.clamp((int) (byte) 0, 52, 9);
    }

    @Test
    public void test120() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test120");
        int int3 = jts.MathUtil.clamp(6, (-9), 35);
    }

    @Test
    public void test121() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test121");
        int int3 = jts.MathUtil.clamp(32, 10, (int) (short) 100);
    }

    @Test
    public void test122() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test122");
        int int3 = jts.MathUtil.clamp(100, (int) (short) -1, (-1));
    }

    @Test
    public void test123() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test123");
        int int3 = jts.MathUtil.clamp(9, 10, (-5));
    }

    @Test
    public void test124() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test124");
        int int3 = jts.MathUtil.clamp((int) 'a', (int) (byte) 1, 2);
    }

    @Test
    public void test125() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test125");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, 0, (-6));
    }

    @Test
    public void test126() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test126");
        int int3 = jts.MathUtil.clamp(5, 1, 10);
    }

    @Test
    public void test127() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test127");
        int int3 = jts.MathUtil.clamp((-4), (int) (short) 1, (int) (short) 1);
    }

    @Test
    public void test128() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test128");
        int int3 = jts.MathUtil.clamp((-2), (-3), 35);
    }

    @Test
    public void test129() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test129");
        int int3 = jts.MathUtil.clamp(3, (int) '4', 32);
    }

    @Test
    public void test130() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test130");
        int int3 = jts.MathUtil.clamp((-9), (-1), 35);
    }

    @Test
    public void test131() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test131");
        int int3 = jts.MathUtil.clamp((int) (short) 10, (-10), (-6));
    }

    @Test
    public void test132() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test132");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (int) (byte) 1, 0);
    }

    @Test
    public void test133() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test133");
        int int3 = jts.MathUtil.clamp((-100), (int) (short) -1, (int) '#');
    }

    @Test
    public void test134() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test134");
        int int3 = jts.MathUtil.clamp(7, (int) (short) 100, (int) '4');
    }

    @Test
    public void test135() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test135");
        int int3 = jts.MathUtil.clamp((-100), (-3), (int) (short) 100);
    }

    @Test
    public void test136() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test136");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 100, (-1));
    }

    @Test
    public void test137() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test137");
        int int3 = jts.MathUtil.clamp((-1), (-7), 100);
    }

    @Test
    public void test138() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test138");
        int int3 = jts.MathUtil.clamp((int) (short) 100, 4, (-5));
    }

    @Test
    public void test139() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test139");
        int int3 = jts.MathUtil.clamp(0, 35, (-4));
    }

    @Test
    public void test140() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test140");
        int int3 = jts.MathUtil.clamp(9, (int) '#', 5);
    }

    @Test
    public void test141() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test141");
        int int3 = jts.MathUtil.clamp((-9), (int) (short) 1, 100);
    }

    @Test
    public void test142() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test142");
        int int3 = jts.MathUtil.clamp(3, (-9), (int) (byte) 1);
    }

    @Test
    public void test143() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test143");
        int int3 = jts.MathUtil.clamp(1, 100, 7);
    }

    @Test
    public void test144() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test144");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (int) (short) 0, 1);
    }

    @Test
    public void test145() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test145");
        int int3 = jts.MathUtil.clamp(35, (-3), (int) (short) -1);
    }

    @Test
    public void test146() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test146");
        int int3 = jts.MathUtil.clamp((int) '4', 4, (-8));
    }

    @Test
    public void test147() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test147");
        int int3 = jts.MathUtil.clamp((int) 'a', (-8), (int) (byte) 100);
    }

    @Test
    public void test148() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test148");
        int int3 = jts.MathUtil.clamp(100, (int) (byte) 100, 0);
    }

    @Test
    public void test149() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test149");
        int int3 = jts.MathUtil.clamp(35, 7, (-3));
    }

    @Test
    public void test150() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test150");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 32, 32);
    }

    @Test
    public void test151() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test151");
        int int3 = jts.MathUtil.clamp(32, (int) (byte) 0, 97);
    }

    @Test
    public void test152() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test152");
        int int3 = jts.MathUtil.clamp((int) (short) 100, (int) (byte) 10, (int) (short) 1);
    }

    @Test
    public void test153() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test153");
        int int3 = jts.MathUtil.clamp(0, (-5), 32);
    }

    @Test
    public void test154() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test154");
        int int3 = jts.MathUtil.clamp((-6), 0, 10);
    }

    @Test
    public void test155() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test155");
        int int3 = jts.MathUtil.clamp(2, 0, (int) (short) 1);
    }

    @Test
    public void test156() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test156");
        int int3 = jts.MathUtil.clamp(100, (int) '#', 52);
    }

    @Test
    public void test157() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test157");
        int int3 = jts.MathUtil.clamp((int) '4', 10, 97);
    }

    @Test
    public void test158() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test158");
        int int3 = jts.MathUtil.clamp(0, 5, 5);
    }

    @Test
    public void test159() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test159");
        int int3 = jts.MathUtil.clamp(35, (int) (byte) 0, 0);
    }

    @Test
    public void test160() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test160");
        int int3 = jts.MathUtil.clamp((-2), 8, (int) 'a');
    }

    @Test
    public void test161() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test161");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, 100, (-2));
    }

    @Test
    public void test162() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test162");
        int int3 = jts.MathUtil.clamp((-10), 4, 9);
    }

    @Test
    public void test163() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test163");
        int int3 = jts.MathUtil.clamp(9, (int) '4', 4);
    }

    @Test
    public void test164() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test164");
        int int3 = jts.MathUtil.clamp((-2), 0, 0);
    }

    @Test
    public void test165() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test165");
        int int3 = jts.MathUtil.clamp(7, (int) (short) 0, (int) 'a');
    }

    @Test
    public void test166() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test166");
        int int3 = jts.MathUtil.clamp(8, (-10), (int) (byte) 100);
    }

    @Test
    public void test167() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test167");
        int int3 = jts.MathUtil.clamp(100, (int) (byte) -1, 32);
    }

    @Test
    public void test168() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test168");
        int int3 = jts.MathUtil.clamp((-2), 100, (-8));
    }

    @Test
    public void test169() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test169");
        int int3 = jts.MathUtil.clamp((int) ' ', 10, 100);
    }

    @Test
    public void test170() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test170");
        int int3 = jts.MathUtil.clamp(3, 0, (int) (short) 1);
    }

    @Test
    public void test171() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test171");
        int int3 = jts.MathUtil.clamp((int) (short) 10, 3, (-2));
    }

    @Test
    public void test172() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test172");
        int int3 = jts.MathUtil.clamp((-3), 3, (-5));
    }

    @Test
    public void test173() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test173");
        int int3 = jts.MathUtil.clamp((int) (short) 1, (int) (short) -1, 9);
    }

    @Test
    public void test174() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test174");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, 7, (int) (short) 0);
    }

    @Test
    public void test175() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test175");
        int int3 = jts.MathUtil.clamp(7, 4, (int) '4');
    }

    @Test
    public void test176() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test176");
        int int3 = jts.MathUtil.clamp(6, (-8), (int) 'a');
    }

    @Test
    public void test177() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test177");
        int int3 = jts.MathUtil.clamp((int) (byte) 0, 0, 10);
    }

    @Test
    public void test178() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test178");
        int int3 = jts.MathUtil.clamp((-1), (int) 'a', (int) (short) 10);
    }

    @Test
    public void test179() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test179");
        int int3 = jts.MathUtil.clamp(3, (-1), (int) 'a');
    }

    @Test
    public void test180() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test180");
        int int3 = jts.MathUtil.clamp(0, 5, (-8));
    }

    @Test
    public void test181() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test181");
        int int3 = jts.MathUtil.clamp((-1), (int) 'a', 0);
    }

    @Test
    public void test182() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test182");
        int int3 = jts.MathUtil.clamp(0, (-9), 100);
    }

    @Test
    public void test183() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test183");
        int int3 = jts.MathUtil.clamp((-100), 9, (-8));
    }

    @Test
    public void test184() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test184");
        int int3 = jts.MathUtil.clamp((-2), (int) (short) 1, 6);
    }

    @Test
    public void test185() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test185");
        int int3 = jts.MathUtil.clamp((-5), 0, 4);
    }

    @Test
    public void test186() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test186");
        int int3 = jts.MathUtil.clamp(1, (int) (short) 1, (int) (byte) 0);
    }

    @Test
    public void test187() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test187");
        int int3 = jts.MathUtil.clamp(35, (-9), 97);
    }

    @Test
    public void test188() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test188");
        int int3 = jts.MathUtil.clamp(100, (-8), (-4));
    }

    @Test
    public void test189() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test189");
        int int3 = jts.MathUtil.clamp((int) (short) 10, 8, (int) (byte) -1);
    }

    @Test
    public void test190() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test190");
        int int3 = jts.MathUtil.clamp((-4), (-4), (-6));
    }

    @Test
    public void test191() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test191");
        int int3 = jts.MathUtil.clamp((-10), (-2), 0);
    }

    @Test
    public void test192() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test192");
        int int3 = jts.MathUtil.clamp(6, (int) 'a', (int) (byte) 1);
    }

    @Test
    public void test193() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test193");
        int int3 = jts.MathUtil.clamp(4, (int) (short) 10, (int) (byte) -1);
    }

    @Test
    public void test194() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test194");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (int) (short) 100, (int) (short) -1);
    }

    @Test
    public void test195() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test195");
        int int3 = jts.MathUtil.clamp((-8), (-100), 0);
    }

    @Test
    public void test196() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test196");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, 35, (int) (short) 0);
    }

    @Test
    public void test197() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test197");
        int int3 = jts.MathUtil.clamp((-1), 0, 0);
    }

    @Test
    public void test198() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test198");
        int int3 = jts.MathUtil.clamp((-1), 10, (-1));
    }

    @Test
    public void test199() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test199");
        int int3 = jts.MathUtil.clamp((-9), (int) (short) 100, (int) (byte) 100);
    }

    @Test
    public void test200() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test200");
        int int3 = jts.MathUtil.clamp(7, (-10), 100);
    }

    @Test
    public void test201() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test201");
        int int3 = jts.MathUtil.clamp(8, (int) '4', 1);
    }

    @Test
    public void test202() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test202");
        int int3 = jts.MathUtil.clamp(8, 2, 0);
    }

    @Test
    public void test203() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test203");
        int int3 = jts.MathUtil.clamp((-4), (-1), (int) (byte) 1);
    }

    @Test
    public void test204() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test204");
        int int3 = jts.MathUtil.clamp(0, (int) (short) 10, 0);
    }

    @Test
    public void test205() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test205");
        int int3 = jts.MathUtil.clamp((-4), 7, (-6));
    }

    @Test
    public void test206() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test206");
        int int3 = jts.MathUtil.clamp(10, (int) '#', 7);
    }

    @Test
    public void test207() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test207");
        int int3 = jts.MathUtil.clamp((-10), (-100), 8);
    }

    @Test
    public void test208() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test208");
        int int3 = jts.MathUtil.clamp((int) '4', 52, (int) 'a');
    }

    @Test
    public void test209() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test209");
        int int3 = jts.MathUtil.clamp(0, (int) 'a', (int) (short) -1);
    }

    @Test
    public void test210() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test210");
        int int3 = jts.MathUtil.clamp(32, 0, 7);
    }

    @Test
    public void test211() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test211");
        int int3 = jts.MathUtil.clamp(52, (-5), (int) ' ');
    }

    @Test
    public void test212() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test212");
        int int3 = jts.MathUtil.clamp(35, 35, (-6));
    }

    @Test
    public void test213() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test213");
        int int3 = jts.MathUtil.clamp((-2), 100, (-5));
    }

    @Test
    public void test214() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test214");
        int int3 = jts.MathUtil.clamp((-7), 2, (-8));
    }

    @Test
    public void test215() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test215");
        int int3 = jts.MathUtil.clamp((-6), (-9), 3);
    }

    @Test
    public void test216() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test216");
        int int3 = jts.MathUtil.clamp((-4), 100, (-1));
    }

    @Test
    public void test217() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test217");
        int int3 = jts.MathUtil.clamp(1, (int) (short) 100, (-4));
    }

    @Test
    public void test218() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test218");
        int int3 = jts.MathUtil.clamp((-4), 10, 32);
    }

    @Test
    public void test219() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test219");
        int int3 = jts.MathUtil.clamp((int) '#', (int) '4', (int) '#');
    }

    @Test
    public void test220() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test220");
        int int3 = jts.MathUtil.clamp((int) '#', 52, (-7));
    }

    @Test
    public void test221() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test221");
        int int3 = jts.MathUtil.clamp((-6), (int) (byte) 100, 0);
    }

    @Test
    public void test222() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test222");
        int int3 = jts.MathUtil.clamp((-9), (-1), 8);
    }

    @Test
    public void test223() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test223");
        int int3 = jts.MathUtil.clamp(6, (-1), (-7));
    }

    @Test
    public void test224() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test224");
        int int3 = jts.MathUtil.clamp(2, 97, (int) (byte) 0);
    }

    @Test
    public void test225() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test225");
        int int3 = jts.MathUtil.clamp(97, (int) (byte) 0, 4);
    }

    @Test
    public void test226() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test226");
        int int3 = jts.MathUtil.clamp((-3), 1, 3);
    }

    @Test
    public void test227() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test227");
        int int3 = jts.MathUtil.clamp((int) 'a', 4, 0);
    }

    @Test
    public void test228() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test228");
        int int3 = jts.MathUtil.clamp((-9), (-2), 97);
    }

    @Test
    public void test229() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test229");
        int int3 = jts.MathUtil.clamp((int) (short) -1, (-1), 0);
    }

    @Test
    public void test230() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test230");
        int int3 = jts.MathUtil.clamp((-1), (int) (byte) 0, (-2));
    }

    @Test
    public void test231() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test231");
        int int3 = jts.MathUtil.clamp((int) ' ', 9, (int) (short) 100);
    }

    @Test
    public void test232() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test232");
        int int3 = jts.MathUtil.clamp((int) '4', (-7), 6);
    }

    @Test
    public void test233() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test233");
        int int3 = jts.MathUtil.clamp(1, 9, (-6));
    }

    @Test
    public void test234() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test234");
        int int3 = jts.MathUtil.clamp(97, (-5), 100);
    }

    @Test
    public void test235() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test235");
        int int3 = jts.MathUtil.clamp(0, (int) (byte) 100, 1);
    }

    @Test
    public void test236() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test236");
        int int3 = jts.MathUtil.clamp((int) (short) 10, (-1), (int) (short) -1);
    }

    @Test
    public void test237() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test237");
        int int3 = jts.MathUtil.clamp(0, (-8), (int) (short) 10);
    }

    @Test
    public void test238() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test238");
        int int3 = jts.MathUtil.clamp((-8), 4, 97);
    }

    @Test
    public void test239() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test239");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, 1, (-1));
    }

    @Test
    public void test240() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test240");
        int int3 = jts.MathUtil.clamp((-9), (int) '4', (int) (byte) 100);
    }

    @Test
    public void test241() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test241");
        int int3 = jts.MathUtil.clamp((-10), (int) (short) 100, 8);
    }

    @Test
    public void test242() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test242");
        int int3 = jts.MathUtil.clamp(35, (int) '4', (-1));
    }

    @Test
    public void test243() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test243");
        int int3 = jts.MathUtil.clamp(2, (-9), 0);
    }

    @Test
    public void test244() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test244");
        int int3 = jts.MathUtil.clamp(100, (-2), 35);
    }

    @Test
    public void test245() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test245");
        int int3 = jts.MathUtil.clamp((int) 'a', 35, (int) (short) 0);
    }

    @Test
    public void test246() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test246");
        int int3 = jts.MathUtil.clamp(8, (-1), (int) (byte) 100);
    }

    @Test
    public void test247() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test247");
        int int3 = jts.MathUtil.clamp(0, 97, 0);
    }

    @Test
    public void test248() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test248");
        int int3 = jts.MathUtil.clamp(5, (int) (short) 0, 6);
    }

    @Test
    public void test249() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test249");
        int int3 = jts.MathUtil.clamp(32, 7, 10);
    }

    @Test
    public void test250() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test250");
        int int3 = jts.MathUtil.clamp(4, (int) (short) 0, (int) (byte) 100);
    }

    @Test
    public void test251() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test251");
        int int3 = jts.MathUtil.clamp((-10), (-100), 97);
    }

    @Test
    public void test252() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test252");
        int int3 = jts.MathUtil.clamp((-10), (int) (byte) 100, 52);
    }

    @Test
    public void test253() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test253");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, 1, (int) '#');
    }

    @Test
    public void test254() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test254");
        int int3 = jts.MathUtil.clamp((int) (short) 1, 1, (-10));
    }

    @Test
    public void test255() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test255");
        int int3 = jts.MathUtil.clamp(3, (int) (short) 0, (int) (short) 10);
    }

    @Test
    public void test256() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test256");
        int int3 = jts.MathUtil.clamp(1, 0, 100);
    }

    @Test
    public void test257() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test257");
        int int3 = jts.MathUtil.clamp(0, (-2), (-5));
    }

    @Test
    public void test258() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test258");
        int int3 = jts.MathUtil.clamp(100, (-1), (int) (byte) 1);
    }

    @Test
    public void test259() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test259");
        int int3 = jts.MathUtil.clamp(35, 100, 0);
    }

    @Test
    public void test260() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test260");
        int int3 = jts.MathUtil.clamp(10, (-3), 52);
    }

    @Test
    public void test261() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test261");
        int int3 = jts.MathUtil.clamp((int) 'a', 100, 9);
    }

    @Test
    public void test262() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test262");
        int int3 = jts.MathUtil.clamp((int) '#', (-100), (-4));
    }

    @Test
    public void test263() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test263");
        int int3 = jts.MathUtil.clamp(1, (int) (byte) 0, (int) (short) -1);
    }

    @Test
    public void test264() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test264");
        int int3 = jts.MathUtil.clamp(2, (int) (byte) -1, 2);
    }

    @Test
    public void test265() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test265");
        int int3 = jts.MathUtil.clamp(0, (-3), (-2));
    }

    @Test
    public void test266() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test266");
        int int3 = jts.MathUtil.clamp(1, 100, (-9));
    }

    @Test
    public void test267() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test267");
        int int3 = jts.MathUtil.clamp(6, (-100), (-10));
    }

    @Test
    public void test268() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test268");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 0, 7);
    }

    @Test
    public void test269() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test269");
        int int3 = jts.MathUtil.clamp((-10), (int) (byte) 10, (int) (short) 1);
    }

    @Test
    public void test270() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test270");
        int int3 = jts.MathUtil.clamp((int) (byte) 10, 9, 35);
    }

    @Test
    public void test271() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test271");
        int int3 = jts.MathUtil.clamp((-10), 0, (int) (byte) 100);
    }

    @Test
    public void test272() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test272");
        int int3 = jts.MathUtil.clamp(5, (int) (byte) 10, (int) (short) -1);
    }

    @Test
    public void test273() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test273");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, (-8), (int) (short) 1);
    }

    @Test
    public void test274() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test274");
        int int3 = jts.MathUtil.clamp(4, (int) (byte) 1, (-7));
    }

    @Test
    public void test275() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test275");
        int int3 = jts.MathUtil.clamp(97, (-3), (-3));
    }

    @Test
    public void test276() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test276");
        int int3 = jts.MathUtil.clamp((-4), (int) '4', 0);
    }

    @Test
    public void test277() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test277");
        int int3 = jts.MathUtil.clamp((-4), (int) (short) 100, (-9));
    }

    @Test
    public void test278() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test278");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (-2), 100);
    }

    @Test
    public void test279() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test279");
        int int3 = jts.MathUtil.clamp(10, 52, (-1));
    }

    @Test
    public void test280() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test280");
        int int3 = jts.MathUtil.clamp(8, (int) (short) -1, 2);
    }

    @Test
    public void test281() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test281");
        int int3 = jts.MathUtil.clamp(8, (int) (short) 100, (int) (short) -1);
    }

    @Test
    public void test282() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test282");
        int int3 = jts.MathUtil.clamp((int) (short) 100, (int) (short) 10, (int) (short) 100);
    }

    @Test
    public void test283() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test283");
        int int3 = jts.MathUtil.clamp((int) ' ', (-100), (int) (short) 1);
    }

    @Test
    public void test284() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test284");
        int int3 = jts.MathUtil.clamp((int) (short) 100, (int) (short) 100, 100);
    }

    @Test
    public void test285() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test285");
        int int3 = jts.MathUtil.clamp((-9), (int) (byte) 1, (int) (byte) 1);
    }

    @Test
    public void test286() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test286");
        int int3 = jts.MathUtil.clamp((-5), (-100), 0);
    }

    @Test
    public void test287() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test287");
        int int3 = jts.MathUtil.clamp((-3), 10, 35);
    }

    @Test
    public void test288() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test288");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (int) (byte) -1, (-100));
    }

    @Test
    public void test289() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test289");
        int int3 = jts.MathUtil.clamp(6, 10, (int) (byte) 10);
    }

    @Test
    public void test290() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test290");
        int int3 = jts.MathUtil.clamp((-8), 100, (int) '4');
    }

    @Test
    public void test291() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test291");
        int int3 = jts.MathUtil.clamp(52, (int) (short) 0, 1);
    }

    @Test
    public void test292() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test292");
        int int3 = jts.MathUtil.clamp(9, 10, 100);
    }

    @Test
    public void test293() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test293");
        int int3 = jts.MathUtil.clamp(10, (int) (byte) 10, (-3));
    }

    @Test
    public void test294() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test294");
        int int3 = jts.MathUtil.clamp((-5), (int) '4', 1);
    }

    @Test
    public void test295() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test295");
        int int3 = jts.MathUtil.clamp((int) (short) 1, 35, (-1));
    }

    @Test
    public void test296() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test296");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (int) (short) 10, 100);
    }

    @Test
    public void test297() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test297");
        int int3 = jts.MathUtil.clamp((int) (short) 0, 5, 35);
    }

    @Test
    public void test298() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test298");
        int int3 = jts.MathUtil.clamp((int) (short) 0, 6, (-4));
    }

    @Test
    public void test299() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test299");
        int int3 = jts.MathUtil.clamp((int) (short) -1, (int) '#', (-4));
    }

    @Test
    public void test300() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test300");
        int int3 = jts.MathUtil.clamp((-1), 32, (int) (byte) -1);
    }

    @Test
    public void test301() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test301");
        int int3 = jts.MathUtil.clamp((int) (short) 10, (-2), (int) '#');
    }

    @Test
    public void test302() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test302");
        int int3 = jts.MathUtil.clamp((int) 'a', 0, (int) (byte) 0);
    }

    @Test
    public void test303() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test303");
        int int3 = jts.MathUtil.clamp(35, (int) (byte) 10, 0);
    }

    @Test
    public void test304() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test304");
        int int3 = jts.MathUtil.clamp(3, (int) (byte) 100, (int) (byte) 100);
    }

    @Test
    public void test305() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test305");
        int int3 = jts.MathUtil.clamp((int) (short) -1, (int) (byte) 100, 10);
    }

    @Test
    public void test306() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test306");
        int int3 = jts.MathUtil.clamp((-100), (int) (short) 0, 0);
    }

    @Test
    public void test307() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test307");
        int int3 = jts.MathUtil.clamp((-1), 0, (-8));
    }

    @Test
    public void test308() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test308");
        int int3 = jts.MathUtil.clamp(100, (int) 'a', (-1));
    }

    @Test
    public void test309() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test309");
        int int3 = jts.MathUtil.clamp((-7), (-6), 0);
    }

    @Test
    public void test310() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test310");
        int int3 = jts.MathUtil.clamp((-2), (-1), (int) '#');
    }

    @Test
    public void test311() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test311");
        int int3 = jts.MathUtil.clamp(97, (int) (byte) 1, 5);
    }

    @Test
    public void test312() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test312");
        int int3 = jts.MathUtil.clamp(100, 10, (int) (byte) -1);
    }

    @Test
    public void test313() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test313");
        int int3 = jts.MathUtil.clamp(3, (-2), 9);
    }

    @Test
    public void test314() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test314");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, 10, 2);
    }

    @Test
    public void test315() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test315");
        int int3 = jts.MathUtil.clamp(2, 4, (int) (byte) 0);
    }

    @Test
    public void test316() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test316");
        int int3 = jts.MathUtil.clamp(5, 2, 32);
    }

    @Test
    public void test317() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test317");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, 32, (int) (byte) -1);
    }

    @Test
    public void test318() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test318");
        int int3 = jts.MathUtil.clamp((-2), (-8), (-6));
    }

    @Test
    public void test319() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test319");
        int int3 = jts.MathUtil.clamp((int) (short) 1, 8, 100);
    }

    @Test
    public void test320() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test320");
        int int3 = jts.MathUtil.clamp((-1), 0, 32);
    }

    @Test
    public void test321() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test321");
        int int3 = jts.MathUtil.clamp((int) (short) 0, 1, (int) ' ');
    }

    @Test
    public void test322() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test322");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 3, (int) (byte) 1);
    }

    @Test
    public void test323() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test323");
        int int3 = jts.MathUtil.clamp((-4), (-9), (int) (short) -1);
    }

    @Test
    public void test324() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test324");
        int int3 = jts.MathUtil.clamp(5, (int) '4', 1);
    }

    @Test
    public void test325() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test325");
        int int3 = jts.MathUtil.clamp((int) 'a', 1, 4);
    }

    @Test
    public void test326() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test326");
        int int3 = jts.MathUtil.clamp((int) 'a', 8, (-3));
    }

    @Test
    public void test327() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test327");
        int int3 = jts.MathUtil.clamp((-4), 6, (-1));
    }

    @Test
    public void test328() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test328");
        int int3 = jts.MathUtil.clamp(5, (-2), (int) 'a');
    }

    @Test
    public void test329() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test329");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, (-1), (-6));
    }

    @Test
    public void test330() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test330");
        int int3 = jts.MathUtil.clamp((-3), 7, 1);
    }

    @Test
    public void test331() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test331");
        int int3 = jts.MathUtil.clamp(8, (-5), 32);
    }

    @Test
    public void test332() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test332");
        int int3 = jts.MathUtil.clamp(100, (-9), 0);
    }

    @Test
    public void test333() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test333");
        int int3 = jts.MathUtil.clamp((int) '4', 9, (-2));
    }

    @Test
    public void test334() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test334");
        int int3 = jts.MathUtil.clamp(32, (int) (short) 0, 100);
    }

    @Test
    public void test335() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test335");
        int int3 = jts.MathUtil.clamp((-4), 9, 32);
    }

    @Test
    public void test336() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test336");
        int int3 = jts.MathUtil.clamp((int) (short) 10, (int) (byte) 10, 1);
    }

    @Test
    public void test337() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test337");
        int int3 = jts.MathUtil.clamp((int) (short) 0, (-2), 4);
    }

    @Test
    public void test338() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test338");
        int int3 = jts.MathUtil.clamp((int) (short) 1, (int) (byte) 100, 2);
    }

    @Test
    public void test339() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test339");
        int int3 = jts.MathUtil.clamp((int) (short) 0, (-100), 5);
    }

    @Test
    public void test340() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test340");
        int int3 = jts.MathUtil.clamp(4, (-3), (-10));
    }

    @Test
    public void test341() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test341");
        int int3 = jts.MathUtil.clamp(97, 10, (int) (byte) 10);
    }

    @Test
    public void test342() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test342");
        int int3 = jts.MathUtil.clamp(52, 35, 1);
    }

    @Test
    public void test343() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test343");
        int int3 = jts.MathUtil.clamp(1, (int) (byte) 1, 1);
    }

    @Test
    public void test344() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test344");
        int int3 = jts.MathUtil.clamp(0, (-2), (int) (byte) 10);
    }

    @Test
    public void test345() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test345");
        int int3 = jts.MathUtil.clamp(35, 2, 100);
    }

    @Test
    public void test346() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test346");
        int int3 = jts.MathUtil.clamp(0, (-2), 3);
    }

    @Test
    public void test347() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test347");
        int int3 = jts.MathUtil.clamp((-6), 10, 4);
    }

    @Test
    public void test348() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test348");
        int int3 = jts.MathUtil.clamp(1, 97, 0);
    }

    @Test
    public void test349() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test349");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 1, 1);
    }

    @Test
    public void test350() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test350");
        int int3 = jts.MathUtil.clamp(35, 97, 10);
    }

    @Test
    public void test351() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test351");
        int int3 = jts.MathUtil.clamp((int) 'a', 100, 7);
    }

    @Test
    public void test352() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test352");
        int int3 = jts.MathUtil.clamp(0, (int) '4', 6);
    }

    @Test
    public void test353() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test353");
        int int3 = jts.MathUtil.clamp(4, (-1), 35);
    }

    @Test
    public void test354() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test354");
        int int3 = jts.MathUtil.clamp((int) (short) -1, (int) '4', (int) (short) 100);
    }

    @Test
    public void test355() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test355");
        int int3 = jts.MathUtil.clamp(5, (int) '4', 7);
    }

    @Test
    public void test356() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test356");
        int int3 = jts.MathUtil.clamp(7, (int) (short) 0, 2);
    }

    @Test
    public void test357() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test357");
        int int3 = jts.MathUtil.clamp(10, (-2), 6);
    }

    @Test
    public void test358() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test358");
        int int3 = jts.MathUtil.clamp(1, 2, (-100));
    }

    @Test
    public void test359() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test359");
        int int3 = jts.MathUtil.clamp(1, 10, 7);
    }

    @Test
    public void test360() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test360");
        int int3 = jts.MathUtil.clamp(8, (-10), (int) (byte) -1);
    }

    @Test
    public void test361() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test361");
        int int3 = jts.MathUtil.clamp(97, 0, 32);
    }

    @Test
    public void test362() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test362");
        int int3 = jts.MathUtil.clamp(0, 4, 0);
    }

    @Test
    public void test363() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test363");
        int int3 = jts.MathUtil.clamp(10, 10, (-10));
    }

    @Test
    public void test364() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test364");
        int int3 = jts.MathUtil.clamp(32, (int) '#', (int) 'a');
    }

    @Test
    public void test365() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test365");
        int int3 = jts.MathUtil.clamp(8, (int) (byte) 0, (-1));
    }

    @Test
    public void test366() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test366");
        int int3 = jts.MathUtil.clamp((-2), (int) ' ', (-4));
    }

    @Test
    public void test367() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test367");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 10, (-4));
    }

    @Test
    public void test368() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test368");
        int int3 = jts.MathUtil.clamp((-1), (int) '4', (int) ' ');
    }

    @Test
    public void test369() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test369");
        int int3 = jts.MathUtil.clamp(0, (-7), (-5));
    }

    @Test
    public void test370() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test370");
        int int3 = jts.MathUtil.clamp((-4), (int) (byte) 100, 0);
    }

    @Test
    public void test371() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test371");
        int int3 = jts.MathUtil.clamp(0, (-4), 97);
    }

    @Test
    public void test372() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test372");
        int int3 = jts.MathUtil.clamp((int) ' ', (-1), 0);
    }

    @Test
    public void test373() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test373");
        int int3 = jts.MathUtil.clamp(3, 5, 0);
    }

    @Test
    public void test374() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test374");
        int int3 = jts.MathUtil.clamp(100, 0, (int) (byte) -1);
    }

    @Test
    public void test375() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test375");
        int int3 = jts.MathUtil.clamp(97, 0, (int) (byte) 100);
    }

    @Test
    public void test376() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test376");
        int int3 = jts.MathUtil.clamp(5, (-8), (-4));
    }

    @Test
    public void test377() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test377");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (int) (byte) 1, 10);
    }

    @Test
    public void test378() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test378");
        int int3 = jts.MathUtil.clamp(3, 7, (int) ' ');
    }

    @Test
    public void test379() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test379");
        int int3 = jts.MathUtil.clamp((int) '4', (-7), (int) (short) 100);
    }

    @Test
    public void test380() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test380");
        int int3 = jts.MathUtil.clamp(0, 6, (int) (byte) 1);
    }

    @Test
    public void test381() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test381");
        int int3 = jts.MathUtil.clamp((-1), (-6), (int) (byte) 100);
    }

    @Test
    public void test382() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test382");
        int int3 = jts.MathUtil.clamp((-3), (-2), (-7));
    }

    @Test
    public void test383() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test383");
        int int3 = jts.MathUtil.clamp((-100), 8, (-7));
    }

    @Test
    public void test384() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test384");
        int int3 = jts.MathUtil.clamp(4, (int) ' ', (int) (byte) 10);
    }

    @Test
    public void test385() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test385");
        int int3 = jts.MathUtil.clamp(2, (int) (short) 100, (int) (byte) 0);
    }

    @Test
    public void test386() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test386");
        int int3 = jts.MathUtil.clamp((int) 'a', (-4), (-6));
    }

    @Test
    public void test387() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test387");
        int int3 = jts.MathUtil.clamp((int) ' ', 1, 100);
    }

    @Test
    public void test388() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test388");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 0, (int) (byte) 10);
    }

    @Test
    public void test389() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test389");
        int int3 = jts.MathUtil.clamp((int) '#', 0, 0);
    }

    @Test
    public void test390() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test390");
        int int3 = jts.MathUtil.clamp(97, 0, 0);
    }

    @Test
    public void test391() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test391");
        int int3 = jts.MathUtil.clamp((-1), 100, 8);
    }

    @Test
    public void test392() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test392");
        int int3 = jts.MathUtil.clamp(0, (int) '#', (-1));
    }

    @Test
    public void test393() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test393");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, (int) (byte) 0, 3);
    }

    @Test
    public void test394() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test394");
        int int3 = jts.MathUtil.clamp((-100), (-2), 5);
    }

    @Test
    public void test395() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test395");
        int int3 = jts.MathUtil.clamp((-6), (-2), (int) (short) 0);
    }

    @Test
    public void test396() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test396");
        int int3 = jts.MathUtil.clamp((-10), (-10), (-8));
    }

    @Test
    public void test397() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test397");
        int int3 = jts.MathUtil.clamp(0, (int) (byte) 10, 100);
    }

    @Test
    public void test398() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test398");
        int int3 = jts.MathUtil.clamp(8, 0, 52);
    }

    @Test
    public void test399() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test399");
        int int3 = jts.MathUtil.clamp(1, 35, (int) 'a');
    }

    @Test
    public void test400() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test400");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (-1), (int) ' ');
    }

    @Test
    public void test401() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test401");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (int) (short) 10, 97);
    }

    @Test
    public void test402() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test402");
        int int3 = jts.MathUtil.clamp(0, (-10), (-10));
    }

    @Test
    public void test403() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test403");
        int int3 = jts.MathUtil.clamp(5, (-3), (-7));
    }

    @Test
    public void test404() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test404");
        int int3 = jts.MathUtil.clamp(4, 100, 0);
    }

    @Test
    public void test405() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test405");
        int int3 = jts.MathUtil.clamp(3, 9, (int) 'a');
    }

    @Test
    public void test406() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test406");
        int int3 = jts.MathUtil.clamp((int) (short) -1, (int) (short) 0, 100);
    }

    @Test
    public void test407() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test407");
        int int3 = jts.MathUtil.clamp(6, 7, 100);
    }

    @Test
    public void test408() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test408");
        int int3 = jts.MathUtil.clamp(9, (int) ' ', (-2));
    }

    @Test
    public void test409() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test409");
        int int3 = jts.MathUtil.clamp((int) ' ', 100, 100);
    }

    @Test
    public void test410() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test410");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, 0, (-3));
    }

    @Test
    public void test411() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test411");
        int int3 = jts.MathUtil.clamp(100, 10, (-3));
    }

    @Test
    public void test412() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test412");
        int int3 = jts.MathUtil.clamp((-9), (int) (byte) 1, 100);
    }

    @Test
    public void test413() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test413");
        int int3 = jts.MathUtil.clamp(1, (int) (byte) 100, (int) (byte) 100);
    }

    @Test
    public void test414() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test414");
        int int3 = jts.MathUtil.clamp((-4), (-100), (-1));
    }

    @Test
    public void test415() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test415");
        int int3 = jts.MathUtil.clamp((int) 'a', (-7), (int) (short) 10);
    }

    @Test
    public void test416() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test416");
        int int3 = jts.MathUtil.clamp((-8), (int) (short) -1, (-6));
    }

    @Test
    public void test417() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test417");
        int int3 = jts.MathUtil.clamp((-3), (-9), 2);
    }

    @Test
    public void test418() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test418");
        int int3 = jts.MathUtil.clamp((-6), 0, 0);
    }

    @Test
    public void test419() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test419");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 10, (-10));
    }

    @Test
    public void test420() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test420");
        int int3 = jts.MathUtil.clamp((-4), (int) (short) 0, (-5));
    }

    @Test
    public void test421() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test421");
        int int3 = jts.MathUtil.clamp((-10), 0, (-7));
    }

    @Test
    public void test422() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test422");
        int int3 = jts.MathUtil.clamp(0, 0, (int) (byte) 1);
    }

    @Test
    public void test423() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test423");
        int int3 = jts.MathUtil.clamp((-3), (-2), 1);
    }

    @Test
    public void test424() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test424");
        int int3 = jts.MathUtil.clamp(3, 0, (int) (byte) -1);
    }

    @Test
    public void test425() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test425");
        int int3 = jts.MathUtil.clamp((-8), 3, (int) (byte) 10);
    }

    @Test
    public void test426() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test426");
        int int3 = jts.MathUtil.clamp((int) 'a', 2, 1);
    }

    @Test
    public void test427() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test427");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, (-6), 5);
    }

    @Test
    public void test428() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test428");
        int int3 = jts.MathUtil.clamp(4, (int) (byte) 100, 10);
    }

    @Test
    public void test429() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test429");
        int int3 = jts.MathUtil.clamp((-2), 0, (-4));
    }

    @Test
    public void test430() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test430");
        int int3 = jts.MathUtil.clamp((int) (short) 0, (int) (short) 0, (int) (byte) -1);
    }

    @Test
    public void test431() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test431");
        int int3 = jts.MathUtil.clamp(100, 10, (int) (short) 100);
    }

    @Test
    public void test432() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test432");
        int int3 = jts.MathUtil.clamp(6, 97, (-2));
    }

    @Test
    public void test433() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test433");
        int int3 = jts.MathUtil.clamp((-4), 10, (-4));
    }

    @Test
    public void test434() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test434");
        int int3 = jts.MathUtil.clamp((int) (short) -1, (int) (byte) 10, (-4));
    }

    @Test
    public void test435() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test435");
        int int3 = jts.MathUtil.clamp(8, (int) (short) 0, 32);
    }

    @Test
    public void test436() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test436");
        int int3 = jts.MathUtil.clamp((-2), 52, (int) (byte) -1);
    }

    @Test
    public void test437() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test437");
        int int3 = jts.MathUtil.clamp((-100), 10, (int) (byte) 10);
    }

    @Test
    public void test438() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test438");
        int int3 = jts.MathUtil.clamp((-7), 1, (int) (short) 0);
    }

    @Test
    public void test439() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test439");
        int int3 = jts.MathUtil.clamp((-2), 1, (-2));
    }

    @Test
    public void test440() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test440");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, (int) (short) 0, 4);
    }

    @Test
    public void test441() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test441");
        int int3 = jts.MathUtil.clamp((int) ' ', (int) 'a', 9);
    }

    @Test
    public void test442() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test442");
        int int3 = jts.MathUtil.clamp((-8), 5, (-1));
    }

    @Test
    public void test443() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test443");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, 0, (-6));
    }

    @Test
    public void test444() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test444");
        int int3 = jts.MathUtil.clamp(4, 5, (-1));
    }

    @Test
    public void test445() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test445");
        int int3 = jts.MathUtil.clamp((int) '#', 5, (-6));
    }

    @Test
    public void test446() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test446");
        int int3 = jts.MathUtil.clamp((int) '#', (int) (short) 100, 0);
    }

    @Test
    public void test447() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test447");
        int int3 = jts.MathUtil.clamp(10, (-8), 1);
    }

    @Test
    public void test448() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test448");
        int int3 = jts.MathUtil.clamp(0, (int) (short) 10, 1);
    }

    @Test
    public void test449() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test449");
        int int3 = jts.MathUtil.clamp((int) (short) 10, 1, 4);
    }

    @Test
    public void test450() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test450");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 32, (-1));
    }

    @Test
    public void test451() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test451");
        int int3 = jts.MathUtil.clamp(3, 5, 100);
    }

    @Test
    public void test452() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test452");
        int int3 = jts.MathUtil.clamp(8, 1, 100);
    }

    @Test
    public void test453() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test453");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, 52, 6);
    }

    @Test
    public void test454() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test454");
        int int3 = jts.MathUtil.clamp(100, 10, 0);
    }

    @Test
    public void test455() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test455");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 10, (-9));
    }

    @Test
    public void test456() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test456");
        int int3 = jts.MathUtil.clamp((int) (byte) 100, 0, 10);
    }

    @Test
    public void test457() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test457");
        int int3 = jts.MathUtil.clamp(9, 52, 10);
    }

    @Test
    public void test458() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test458");
        int int3 = jts.MathUtil.clamp(97, (-100), 10);
    }

    @Test
    public void test459() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test459");
        int int3 = jts.MathUtil.clamp((-4), 0, (-4));
    }

    @Test
    public void test460() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test460");
        int int3 = jts.MathUtil.clamp((int) 'a', 3, (-6));
    }

    @Test
    public void test461() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test461");
        int int3 = jts.MathUtil.clamp((-1), (int) (short) 100, (-4));
    }

    @Test
    public void test462() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test462");
        int int3 = jts.MathUtil.clamp(0, (int) (byte) -1, (-3));
    }

    @Test
    public void test463() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test463");
        int int3 = jts.MathUtil.clamp((int) (byte) 0, (int) (byte) 10, (int) (byte) 1);
    }

    @Test
    public void test464() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test464");
        int int3 = jts.MathUtil.clamp((-9), 6, 6);
    }

    @Test
    public void test465() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test465");
        int int3 = jts.MathUtil.clamp(3, (int) (byte) -1, (int) (byte) 100);
    }

    @Test
    public void test466() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test466");
        int int3 = jts.MathUtil.clamp(1, (int) '#', 52);
    }

    @Test
    public void test467() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test467");
        int int3 = jts.MathUtil.clamp(0, (int) ' ', (-9));
    }

    @Test
    public void test468() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test468");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 5, (int) (short) 100);
    }

    @Test
    public void test469() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test469");
        int int3 = jts.MathUtil.clamp((int) (byte) 1, (-100), 1);
    }

    @Test
    public void test470() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test470");
        int int3 = jts.MathUtil.clamp((-1), 7, 52);
    }

    @Test
    public void test471() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test471");
        int int3 = jts.MathUtil.clamp((int) (byte) 10, 100, (int) (byte) -1);
    }

    @Test
    public void test472() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test472");
        int int3 = jts.MathUtil.clamp(5, 100, (int) (short) -1);
    }

    @Test
    public void test473() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test473");
        int int3 = jts.MathUtil.clamp((-8), 6, (int) (byte) 0);
    }

    @Test
    public void test474() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test474");
        int int3 = jts.MathUtil.clamp(0, 0, (-9));
    }

    @Test
    public void test475() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test475");
        int int3 = jts.MathUtil.clamp((-8), 52, 6);
    }

    @Test
    public void test476() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test476");
        int int3 = jts.MathUtil.clamp(100, 7, (int) (short) 0);
    }

    @Test
    public void test477() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test477");
        int int3 = jts.MathUtil.clamp(9, 0, (int) (byte) 10);
    }

    @Test
    public void test478() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test478");
        int int3 = jts.MathUtil.clamp((int) (short) 10, 0, (-6));
    }

    @Test
    public void test479() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test479");
        int int3 = jts.MathUtil.clamp(0, 10, 35);
    }

    @Test
    public void test480() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test480");
        int int3 = jts.MathUtil.clamp(0, 1, 0);
    }

    @Test
    public void test481() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test481");
        int int3 = jts.MathUtil.clamp(4, (int) (short) -1, (-1));
    }

    @Test
    public void test482() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test482");
        int int3 = jts.MathUtil.clamp(0, (int) (short) 10, 10);
    }

    @Test
    public void test483() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test483");
        int int3 = jts.MathUtil.clamp((-1), (int) (byte) 1, (int) '4');
    }

    @Test
    public void test484() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test484");
        int int3 = jts.MathUtil.clamp((int) (short) 100, 10, 100);
    }

    @Test
    public void test485() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test485");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 0, (-8));
    }

    @Test
    public void test486() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test486");
        int int3 = jts.MathUtil.clamp((int) (byte) 10, 5, (-1));
    }

    @Test
    public void test487() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test487");
        int int3 = jts.MathUtil.clamp((int) (byte) -1, (int) (short) 10, 10);
    }

    @Test
    public void test488() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test488");
        int int3 = jts.MathUtil.clamp(10, 97, (-3));
    }

    @Test
    public void test489() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test489");
        int int3 = jts.MathUtil.clamp(35, (-10), (int) (short) 100);
    }

    @Test
    public void test490() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test490");
        int int3 = jts.MathUtil.clamp(0, 0, 5);
    }

    @Test
    public void test491() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test491");
        int int3 = jts.MathUtil.clamp((int) (short) -1, 100, 10);
    }

    @Test
    public void test492() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test492");
        int int3 = jts.MathUtil.clamp(10, (-8), (int) (short) 100);
    }

    @Test
    public void test493() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test493");
        int int3 = jts.MathUtil.clamp((int) (short) 1, 0, (int) (short) 10);
    }

    @Test
    public void test494() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test494");
        int int3 = jts.MathUtil.clamp((-4), 0, (int) 'a');
    }

    @Test
    public void test495() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test495");
        int int3 = jts.MathUtil.clamp(100, 32, 3);
    }

    @Test
    public void test496() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test496");
        int int3 = jts.MathUtil.clamp((int) '4', (-6), 10);
    }

    @Test
    public void test497() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test497");
        int int3 = jts.MathUtil.clamp((-9), 35, (int) (short) 10);
    }

    @Test
    public void test498() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test498");
        int int3 = jts.MathUtil.clamp((-7), 1, (-5));
    }

    @Test
    public void test499() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "MathUtilTester0.test499");
        int int3 = jts.MathUtil.clamp((-1), 2, (int) (short) 0);
    }
}

